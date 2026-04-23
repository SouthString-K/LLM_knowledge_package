#!/usr/bin/env python
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
RAW_SOURCES_DIR = ROOT / "raw" / "sources"
INDEX_PATH = ROOT / "index.md"
LOG_PATH = ROOT / "log.md"

REQUIRED_FIELDS = {"title", "type", "created", "updated", "tags", "confidence"}
SECTION_ORDER = [
    ("entities", "实体"),
    ("concepts", "概念"),
    ("sources", "资料"),
    ("comparisons", "对比"),
    ("synthesis", "综合"),
    ("retrospectives", "复盘"),
    ("misc", "其他"),
]


@dataclass
class WikiPage:
    path: Path
    slug: str
    section: str
    frontmatter: Dict[str, object]
    body: str
    links: Set[str]

    @property
    def title(self) -> str:
        return str(self.frontmatter.get("title", self.slug))

    @property
    def page_type(self) -> str:
        return str(self.frontmatter.get("type", "")).strip()

    @property
    def updated(self) -> str:
        return str(self.frontmatter.get("updated", ""))

    @property
    def created(self) -> str:
        return str(self.frontmatter.get("created", ""))

    @property
    def confidence(self) -> str:
        return str(self.frontmatter.get("confidence", ""))

    @property
    def tags(self) -> List[str]:
        tags = self.frontmatter.get("tags", [])
        if isinstance(tags, list):
            return [str(tag) for tag in tags]
        if isinstance(tags, str) and tags:
            return [tags]
        return []

    @property
    def related(self) -> List[str]:
        related = self.frontmatter.get("related", [])
        if isinstance(related, list):
            return [str(item) for item in related]
        if isinstance(related, str) and related:
            return [related]
        return []

    @property
    def source_refs(self) -> List[str]:
        refs = self.frontmatter.get("source-ref", [])
        if isinstance(refs, list):
            return [str(item) for item in refs]
        if isinstance(refs, str) and refs:
            return [refs]
        return []

    def summary(self) -> str:
        for raw_line in self.body.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith(("#", "|", "---", "```")):
                continue
            if line.startswith(("- ", "* ")):
                compact = re.sub(r"\s+", " ", line[2:].strip())
                return compact[:72]
            if re.match(r"^\d+\.\s+", line):
                compact = re.sub(r"\s+", " ", re.sub(r"^\d+\.\s+", "", line))
                return compact[:72]
            if line.startswith("*本页由") or line.startswith("*概念页由") or line.startswith("*实体页由"):
                continue
            compact = re.sub(r"\s+", " ", line)
            return compact[:72]

        for raw_line in self.body.splitlines():
            line = raw_line.strip()
            if not (line.startswith("|") and line.endswith("|")):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) < 2:
                continue
            if set("".join(cells)) <= {"-", " "}:
                continue
            if cells[0] in {"项目", "指标", "模块", "价值", "方法", "版本", "架构"}:
                continue
            compact = re.sub(r"\s+", " ", f"{cells[0]}：{cells[1]}")
            return compact[:72]
        return "—"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="LabNotes wiki maintenance tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("lint", help="检查 wiki 健康状态")

    build_index = subparsers.add_parser("build-index", help="重建 index.md")
    build_index.add_argument(
        "--write",
        action="store_true",
        help="写回 index.md；默认只输出预览",
    )

    query = subparsers.add_parser("query", help="基于现有 wiki 做本地检索式问答")
    query.add_argument("question", help="要查询的问题")
    query.add_argument(
        "--top-k",
        type=int,
        default=3,
        help="返回最相关页面数量，默认 3",
    )

    ingest = subparsers.add_parser("ingest", help="把原始资料生成 source 页面并更新日志")
    ingest.add_argument("source_path", help="原始资料路径，支持 md/txt/pdf")
    ingest.add_argument(
        "--top-k",
        type=int,
        default=4,
        help="自动关联的已有页面数量，默认 4",
    )

    return parser.parse_args()


def configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def iter_markdown_files(folder: Path) -> List[Path]:
    return sorted(
        path
        for path in folder.rglob("*.md")
        if path.is_file() and path.name != ".gitkeep"
    )


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text

    frontmatter_lines: List[str] = []
    body_start = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            body_start = index + 1
            break
        frontmatter_lines.append(lines[index])

    if body_start is None:
        return {}, text

    frontmatter = parse_yaml_like_lines(frontmatter_lines)
    body = "\n".join(lines[body_start:]).lstrip("\n")
    return frontmatter, body


def parse_yaml_like_lines(lines: List[str]) -> Dict[str, object]:
    result: Dict[str, object] = {}
    current_key: Optional[str] = None

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("- ") and current_key:
            result.setdefault(current_key, [])
            value = parse_scalar(stripped[2:].strip())
            existing = result[current_key]
            if not isinstance(existing, list):
                existing = [existing]
            existing.append(value)
            result[current_key] = existing
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        current_key = key.strip()
        value = value.strip()
        if not value:
            result[current_key] = []
            continue

        result[current_key] = parse_scalar(value)

    return result


def parse_scalar(value: str) -> object:
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in split_list_items(inner)]

    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]

    return value


def split_list_items(text: str) -> List[str]:
    items: List[str] = []
    current: List[str] = []
    in_quote = False
    quote_char = ""

    for char in text:
        if char in {'"', "'"}:
            if in_quote and char == quote_char:
                in_quote = False
                quote_char = ""
            elif not in_quote:
                in_quote = True
                quote_char = char
        if char == "," and not in_quote:
            items.append("".join(current).strip())
            current = []
            continue
        current.append(char)

    if current:
        items.append("".join(current).strip())

    return [item for item in items if item]


def extract_links(body: str) -> Set[str]:
    links = set(re.findall(r"\[\[([^\]|#]+)", body))
    return {link.strip() for link in links if link.strip()}


def load_pages() -> Dict[str, WikiPage]:
    pages: Dict[str, WikiPage] = {}
    for path in iter_markdown_files(WIKI_DIR):
        text = path.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(text)
        slug = path.stem
        section = path.parent.name
        links = extract_links(body)
        pages[slug] = WikiPage(
            path=path,
            slug=slug,
            section=section,
            frontmatter=frontmatter,
            body=body,
            links=links,
        )
    return pages


def validate_frontmatter(page: WikiPage) -> List[str]:
    issues: List[str] = []
    missing = sorted(field for field in REQUIRED_FIELDS if field not in page.frontmatter)
    if missing:
        issues.append(f"{page.slug}: 缺少 frontmatter 字段 {', '.join(missing)}")

    if page.page_type and page.page_type not in {"entity", "concept", "source", "comparison", "synthesis", "retrospective", "misc"}:
        issues.append(f"{page.slug}: type `{page.page_type}` 不在约定范围内")

    if page.page_type == "source" and not page.source_refs:
        issues.append(f"{page.slug}: source 页面缺少 source-ref")

    return issues


def build_backlinks(pages: Dict[str, WikiPage]) -> Dict[str, Set[str]]:
    backlinks = {slug: set() for slug in pages}
    for slug, page in pages.items():
        refs = set(page.related) | page.links
        for ref in refs:
            if ref in backlinks:
                backlinks[ref].add(slug)
    return backlinks


def lint_pages(pages: Dict[str, WikiPage]) -> int:
    frontmatter_issues: List[str] = []
    dead_links: List[str] = []
    orphan_pages: List[str] = []
    contradiction_hits: List[str] = []
    outdated_hits: List[str] = []
    uncovered_sources: List[str] = []

    backlinks = build_backlinks(pages)
    referenced_source_paths: Set[str] = set()

    for page in pages.values():
        frontmatter_issues.extend(validate_frontmatter(page))

        refs = set(page.related) | page.links
        for ref in sorted(refs):
            if ref not in pages:
                dead_links.append(f"{page.slug}: 引用了不存在的页面 `{ref}`")

        if not refs and not backlinks.get(page.slug):
            orphan_pages.append(page.slug)

        if "[CONTRADICTION]" in page.body:
            contradiction_hits.append(page.slug)
        if "[OUTDATED]" in page.body:
            outdated_hits.append(page.slug)

        if page.page_type == "source":
            referenced_source_paths.update(page.source_refs)

    for raw_path in iter_markdown_files(RAW_SOURCES_DIR):
        rel_path = raw_path.relative_to(ROOT).as_posix()
        if rel_path not in referenced_source_paths:
            uncovered_sources.append(rel_path)

    for raw_path in RAW_SOURCES_DIR.rglob("*.pdf"):
        if raw_path.is_file():
            rel_path = raw_path.relative_to(ROOT).as_posix()
            if rel_path not in referenced_source_paths:
                uncovered_sources.append(rel_path)

    print(f"## Lint 报告 — {date.today().isoformat()}")
    print()

    print("### 🔴 需要立即处理")
    if frontmatter_issues or dead_links:
        for issue in frontmatter_issues:
            print(f"- {issue}")
        for issue in dead_links:
            print(f"- {issue}")
    else:
        print("- 暂无 frontmatter / 死链问题")
    print()

    print("### 🟡 可以优化")
    if orphan_pages:
        print(f"- 孤立页面：{', '.join(orphan_pages)}")
    if uncovered_sources:
        print(f"- 尚未 ingest 的原始资料：{', '.join(sorted(set(uncovered_sources)))}")
    if contradiction_hits:
        print(f"- 含 [CONTRADICTION] 标记页面：{', '.join(sorted(contradiction_hits))}")
    if outdated_hits:
        print(f"- 含 [OUTDATED] 标记页面：{', '.join(sorted(outdated_hits))}")
    if not any([orphan_pages, uncovered_sources, contradiction_hits, outdated_hits]):
        print("- 暂无明显优化项")
    print()

    healthy_count = sum(
        1
        for slug, page in pages.items()
        if not validate_frontmatter(page)
        and not ((set(page.related) | page.links) - pages.keys())
    )

    print("### 🟢 健康")
    print(f"- {healthy_count} 个页面结构正常")

    has_errors = bool(frontmatter_issues or dead_links)
    return 1 if has_errors else 0


def build_index_markdown(pages: Dict[str, WikiPage]) -> str:
    total_pages = len(pages)
    latest_update = max((page.updated for page in pages.values()), default="—")
    lines = [
        "# 知识库总索引",
        "",
        f"> 最后更新：{latest_update} | 共 {total_pages} 个页面",
        "",
        "---",
        "",
    ]

    pages_by_section: Dict[str, List[WikiPage]] = {section: [] for section, _ in SECTION_ORDER}
    for page in pages.values():
        pages_by_section.setdefault(page.section, []).append(page)

    for section, label in SECTION_ORDER:
        section_pages = sorted(
            pages_by_section.get(section, []),
            key=lambda item: item.path.name,
        )
        real_pages = [page for page in section_pages if page.path.name != ".gitkeep"]
        lines.append(f"## {section_emoji(section)} {label}（{len(real_pages)} 个）")
        lines.append("")

        if not real_pages:
            if section == "retrospectives":
                lines.append("| 页面 | 日期 |")
                lines.append("|------|------|")
                lines.append("| （暂无） | — |")
            elif section == "sources":
                lines.append("| 页面 | 日期 | 关键要点 | 状态 |")
                lines.append("|------|------|----------|------|")
                lines.append("| （暂无） | — | — | — |")
            else:
                lines.append("| 页面 | 摘要 | 标签 | 置信度 |")
                lines.append("|------|------|------|--------|")
                lines.append("| （暂无） | — | — | — |")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue

        if section == "sources":
            lines.append("| 页面 | 日期 | 关键要点 | 状态 |")
            lines.append("|------|------|----------|------|")
            for page in real_pages:
                status = "已 ingest" if page.source_refs else "待补充"
                lines.append(
                    f"| [{page.slug}](wiki/{section}/{page.path.name}) | {page.created or '—'} | {escape_pipes(page.summary())} | {status} |"
                )
        elif section == "retrospectives":
            lines.append("| 页面 | 日期 |")
            lines.append("|------|------|")
            for page in real_pages:
                lines.append(
                    f"| [{page.slug}](wiki/{section}/{page.path.name}) | {page.created or '—'} |"
                )
        else:
            lines.append("| 页面 | 摘要 | 标签 | 置信度 |")
            lines.append("|------|------|------|--------|")
            for page in real_pages:
                tags = " ".join(f"#{tag}" for tag in page.tags[:4]) or "—"
                lines.append(
                    f"| [{page.slug}](wiki/{section}/{page.path.name}) | {escape_pipes(page.summary())} | {escape_pipes(tags)} | {page.confidence or '—'} |"
                )

        lines.append("")
        lines.append("---")
        lines.append("")

    raw_files = [path for path in RAW_SOURCES_DIR.rglob("*") if path.is_file() and path.name != ".gitkeep"]
    lines.extend(
        [
            "## 📊 知识库状态",
            "",
            "| 指标 | 值 |",
            "|------|---|",
            f"| 原始资料总数 | {len(raw_files)} |",
            f"| Wiki 页面总数 | {total_pages} |",
            f"| 最后 ingest | {latest_update} |",
            f"| 最后 lint | {date.today().isoformat()} |",
            "",
            "---",
            "",
            "*此文件可由 `python scripts/wiki_tools.py build-index --write` 自动重建*",
        ]
    )

    return "\n".join(lines) + "\n"


def section_emoji(section: str) -> str:
    mapping = {
        "entities": "🧑",
        "concepts": "📚",
        "sources": "📄",
        "comparisons": "⚖️",
        "synthesis": "🧠",
        "retrospectives": "🔄",
        "misc": "🗂️",
    }
    return mapping.get(section, "📁")


def escape_pipes(text: str) -> str:
    return text.replace("|", "\\|")


def tokenize_query(question: str) -> List[str]:
    raw_tokens = re.findall(r"[\u4e00-\u9fff]+|[A-Za-z0-9_-]+", question.lower())
    tokens: List[str] = []

    for token in raw_tokens:
        cleaned = token.strip()
        if len(cleaned) <= 1:
            continue
        tokens.append(cleaned)

        if re.fullmatch(r"[\u4e00-\u9fff]+", cleaned) and len(cleaned) > 2:
            max_window = min(4, len(cleaned))
            for window in range(2, max_window + 1):
                for index in range(0, len(cleaned) - window + 1):
                    chunk = cleaned[index : index + window]
                    if chunk not in tokens:
                        tokens.append(chunk)

    return tokens


def slugify(text: str) -> str:
    normalized = text.lower().strip()
    normalized = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized)
    normalized = normalized.strip("-_")
    return normalized or "untitled"


def unique_preserve_order(items: List[str]) -> List[str]:
    seen: Set[str] = set()
    result: List[str] = []
    for item in items:
        if item in seen or not item:
            continue
        seen.add(item)
        result.append(item)
    return result


def resolve_source_path(path_str: str) -> Path:
    path = Path(path_str)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def read_markdown_or_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("当前环境缺少 pypdf，无法读取 PDF。") from exc

    reader = PdfReader(str(path))
    pages: List[str] = []
    for page in reader.pages:
        extracted = page.extract_text() or ""
        if extracted.strip():
            pages.append(extracted.strip())
    return "\n\n".join(pages)


def read_source_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        return read_markdown_or_text(path)
    if suffix == ".pdf":
        return read_pdf_text(path)
    raise RuntimeError(f"暂不支持的文件类型：{path.suffix}")


def extract_title(text: str, fallback: str) -> str:
    for raw_line in text.splitlines():
        line = raw_line.strip().lstrip("#").strip()
        if not line:
            continue
        if len(line) < 6:
            continue
        if len(line) > 220:
            continue
        if line.startswith(("Abstract", "摘要", "关键词", "Index Terms")):
            continue
        return re.sub(r"\s+", " ", line)
    return fallback


def summarize_text(text: str, max_sentences: int = 3, max_chars: int = 520) -> str:
    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        return "原始资料已导入，但暂未成功提取可用摘要。"

    parts = re.split(r"(?<=[。！？.!?])\s+", cleaned)
    summary_parts: List[str] = []
    current_len = 0
    for part in parts:
        sentence = part.strip()
        if not sentence:
            continue
        summary_parts.append(sentence)
        current_len += len(sentence)
        if len(summary_parts) >= max_sentences or current_len >= max_chars:
            break

    summary = " ".join(summary_parts).strip()
    if not summary:
        summary = cleaned[:max_chars]
    return summary[:max_chars]


def infer_related_pages_from_text(
    pages: Dict[str, WikiPage], text: str, title: str, top_k: int
) -> List[WikiPage]:
    tokens = tokenize_query(f"{title} {text[:3000]}")
    scored = []
    for page in pages.values():
        score = score_page(page, title, tokens) + score_page(page, text[:2000], tokens)
        if score > 0:
            scored.append((score, page))

    scored.sort(key=lambda item: (-item[0], item[1].slug))
    return [page for _, page in scored[: max(top_k, 1)]]


def infer_tags(related_pages: List[WikiPage], source_path: Path) -> List[str]:
    tags: List[str] = []
    for page in related_pages:
        tags.extend(page.tags[:2])

    stem_tokens = re.findall(r"[A-Za-z0-9_-]+", source_path.stem)
    tags.extend(stem_tokens[:3])
    return unique_preserve_order(tags)[:5]


def detect_existing_source_page(
    pages: Dict[str, WikiPage], rel_source_path: str
) -> Optional[WikiPage]:
    for page in pages.values():
        if page.page_type != "source":
            continue
        if rel_source_path in page.source_refs:
            return page
    return None


def build_source_page_content(
    title: str,
    today: str,
    tags: List[str],
    related_slugs: List[str],
    rel_source_path: str,
    aliases: List[str],
    summary: str,
    related_pages: List[WikiPage],
) -> str:
    tags_str = ", ".join(tags) if tags else "source"
    aliases_str = ", ".join(f'"{alias}"' for alias in aliases)

    lines = [
        "---",
        f'title: "{title}"',
        "type: source",
        f"created: {today}",
        f"updated: {today}",
        f"tags: [{tags_str}]",
        "related:",
    ]

    for slug in related_slugs:
        lines.append(f"  - {slug}")

    lines.extend(
        [
            "confidence: medium",
            "source-ref:",
            f"  - {rel_source_path}",
            f"aliases: [{aliases_str}]",
            "---",
            "",
            "# 资料摘要",
            "",
            summary,
            "",
            "# 来源信息",
            "",
            f"- 原始文件：`{rel_source_path}`",
            "",
            "# 关联页面",
            "",
        ]
    )

    if related_pages:
        for page in related_pages:
            lines.append(f"- [[{page.slug}]] — {page.title}")
    else:
        lines.append("- （暂无自动识别出的关联页面）")

    lines.extend(["", "---", "", "*本页由 ingest 工具自动生成，可继续手工补充细节*"])
    return "\n".join(lines) + "\n"


def insert_log_entry(entry: str) -> None:
    text = LOG_PATH.read_text(encoding="utf-8")
    marker = "## 历史记录"
    if marker not in text:
        LOG_PATH.write_text(text.rstrip() + "\n\n" + entry + "\n", encoding="utf-8")
        return

    head, tail = text.split(marker, 1)
    new_text = head + marker + "\n\n" + entry.strip() + "\n\n" + tail.lstrip("\n")
    LOG_PATH.write_text(new_text, encoding="utf-8")


def build_log_entry(
    today: str,
    rel_source_path: str,
    title: str,
    source_slug: str,
    related_pages: List[WikiPage],
) -> str:
    lines = [
        f"## [{today}] ingest | 新资料：{title}",
        "",
        f"**原始资料：** `{rel_source_path}`",
        "",
        f"**资料页：** `{source_slug}`",
        "",
    ]

    if related_pages:
        lines.append("**自动关联页面：**")
        for page in related_pages:
            lines.append(f"- {page.slug}")
        lines.append("")

    lines.extend(
        [
            "**更新页面：**",
            "- log.md",
            "- index.md",
            f"- wiki/sources/{source_slug}.md",
        ]
    )
    return "\n".join(lines)


def score_page(page: WikiPage, question: str, tokens: List[str]) -> int:
    question_lower = question.lower().strip()
    title = page.title.lower()
    slug = page.slug.lower()
    tags = " ".join(page.tags).lower()
    related = " ".join(page.related).lower()
    summary = page.summary().lower()
    body = page.body.lower()

    score = 0
    if question_lower:
        score += title.count(question_lower) * 20
        score += summary.count(question_lower) * 12
        score += body.count(question_lower) * 6

    for token in tokens:
        score += title.count(token) * 8
        score += slug.count(token) * 7
        score += tags.count(token) * 6
        score += related.count(token) * 3
        score += summary.count(token) * 4
        score += body.count(token)

    return score


def extract_snippet(page: WikiPage, tokens: List[str]) -> str:
    for raw_line in page.body.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("#", "---", "```", "|")):
            continue
        normalized = line.lower()
        if not tokens or any(token in normalized for token in tokens):
            compact = re.sub(r"\s+", " ", line)
            return compact[:120]
    return page.summary()


def confidence_label(results: List[Tuple[int, WikiPage]]) -> str:
    if not results:
        return "低：当前知识库中没有匹配到明显相关页面。"

    top_score = results[0][0]
    if top_score >= 30 and len(results) >= 2 and results[1][0] > 0:
        return "高：命中了多个相关页面，且关键词重合度较高。"
    if top_score >= 12:
        return "中：命中了相关页面，但覆盖面或重合度有限。"
    return "低：仅命中了弱相关页面，建议补充资料后再问。"


def run_query(pages: Dict[str, WikiPage], question: str, top_k: int) -> int:
    tokens = tokenize_query(question)
    scored_pages = []
    for page in pages.values():
        score = score_page(page, question, tokens)
        if score > 0:
            scored_pages.append((score, page))

    scored_pages.sort(key=lambda item: (-item[0], item[1].slug))
    results = scored_pages[: max(top_k, 1)]

    print(f"## 回答：{question}")
    print()
    print("### 回答内容")
    if not results:
        print("当前知识库里还没有足够相关的页面来回答这个问题。你可以先 ingest 新资料，或者换一个更贴近现有主题的问题。")
    else:
        for _, page in results:
            print(f"- {page.title}：{extract_snippet(page, tokens)}")
    print()

    print("### 引用溯源")
    if not results:
        print("- 暂无可引用页面")
    else:
        for _, page in results:
            rel_path = page.path.relative_to(ROOT).as_posix()
            print(f"- [{page.title}]({rel_path}) — 命中页面 `{page.slug}`，用于支持当前回答。")
    print()

    print("### 置信度")
    print(confidence_label(results))
    print()
    print("---")
    print("💡 如果这个回答有价值，我建议整理成 comparison 或 synthesis 页面写回 wiki。")
    return 0


def run_ingest(pages: Dict[str, WikiPage], source_path_str: str, top_k: int) -> int:
    source_path = resolve_source_path(source_path_str)
    if not source_path.exists():
        print(f"找不到原始资料：{source_path}")
        return 1

    rel_source_path = source_path.relative_to(ROOT).as_posix()
    existing_page = detect_existing_source_page(pages, rel_source_path)
    if existing_page:
        print(f"该原始资料已经存在资料页：{existing_page.slug}")
        print(existing_page.path.relative_to(ROOT).as_posix())
        return 0

    text = read_source_text(source_path)
    title = extract_title(text, source_path.stem)
    summary = summarize_text(text)
    today = date.today().isoformat()
    source_slug = f"source-{today}-{slugify(source_path.stem)}"
    page_path = WIKI_DIR / "sources" / f"{source_slug}.md"
    counter = 2
    while page_path.exists():
        page_path = WIKI_DIR / "sources" / f"{source_slug}-{counter}.md"
        counter += 1

    final_slug = page_path.stem
    related_pages = infer_related_pages_from_text(pages, text, title, top_k=top_k)
    related_slugs = [page.slug for page in related_pages]
    tags = infer_tags(related_pages, source_path)
    aliases = unique_preserve_order([source_path.stem, title])[:4]

    content = build_source_page_content(
        title=title,
        today=today,
        tags=tags,
        related_slugs=related_slugs,
        rel_source_path=rel_source_path,
        aliases=aliases,
        summary=summary,
        related_pages=related_pages,
    )
    page_path.write_text(content, encoding="utf-8")

    log_entry = build_log_entry(
        today=today,
        rel_source_path=rel_source_path,
        title=title,
        source_slug=final_slug,
        related_pages=related_pages,
    )
    try:
        insert_log_entry(log_entry)
    except PermissionError:
        print(f"提示：当前环境无法直接写入 {LOG_PATH.name}，资料页已生成，可稍后补记日志。")

    updated_pages = load_pages()
    run_build_index(updated_pages, write=True)

    print(f"已生成资料页：{page_path.relative_to(ROOT).as_posix()}")
    return 0


def run_build_index(pages: Dict[str, WikiPage], write: bool) -> int:
    content = build_index_markdown(pages)
    if write:
        try:
            INDEX_PATH.write_text(content, encoding="utf-8")
        except PermissionError:
            print(f"无法直接写入 {INDEX_PATH}，下面输出生成结果供手动应用：")
            print()
            print(content)
            return 1
        print(f"已更新 {INDEX_PATH}")
        return 0

    print(content)
    return 0


def main() -> int:
    configure_stdout()
    args = parse_args()
    pages = load_pages()

    if args.command == "lint":
        return lint_pages(pages)

    if args.command == "build-index":
        return run_build_index(pages, write=args.write)

    if args.command == "query":
        return run_query(pages, question=args.question, top_k=args.top_k)

    if args.command == "ingest":
        return run_ingest(pages, source_path_str=args.source_path, top_k=args.top_k)

    return 1


if __name__ == "__main__":
    sys.exit(main())
