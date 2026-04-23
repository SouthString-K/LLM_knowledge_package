# 🧠 第二大脑 

> 用长上下文 LLM 直接阅读整个知识库，用纯 Markdown 构建，Obsidian 可视化

---

## 🎯 目标

打造一个**越来越懂你**的个人知识库：
- **积累性**——每次交互都在让知识库更丰富
- **准确性**——错误信息及时清理，矛盾及时标注
- **可追溯**——所有知识都有来源，可溯源
- **可视化**——用 Obsidian 图谱直观查看知识结构

---

## 📁 目录结构

```
E:\LabNotes\
│
├── raw/                        # 原始资料（不可变）
│   ├── sources/                # 源文档：文章、论文、笔记
│   └── assets/                 # 附件：图片等
│
├── wiki/                       # LLM 维护的知识库
│   ├── entities/               # 实体页：人、物、地点、事件
│   ├── concepts/               # 概念页：主题、理论、方法
│   ├── sources/                # 资料摘要页
│   ├── comparisons/            # 对比分析页
│   ├── synthesis/              # 综合分析页
│   ├── retrospectives/         # 复盘页
│   └── misc/                   # 其他
│
├── archive/                    # 旧内容归档区
│   └── legacy_notes/           # 历史笔记、旧资料、旧附件
│
├── scripts/                    # 辅助脚本
├── 知识库.base                 # Obsidian Bases 数据视图入口
├── index.md                    # 知识库总索引
├── log.md                      # 操作日志
├── PROFILE.md                  # 主人画像（第二大脑了解你）
└── CLAUDE.md                   # LLM 维护规范（本文件）
```

---

## 🚀 快速开始

### 1. 初始化（第一次使用）

1. 打开 `PROFILE.md`，告诉我你的背景，我来填写
2. 放入第一份资料到 `raw/sources/`
3. 说：`"帮我 ingest 这个"`

### 2. 日常使用

| 操作 | 怎么说 |
|------|--------|
| 摄入新资料 | `"帮我 ingest [文件名]"` |
| 问问题 | `"基于知识库回答：xxx"` |
| 健康检查 | `"lint 一下"` |
| 周复盘 | `"这周复盘一下"` |
| 月复盘 | `"本月复盘"` |

### 3. 用 Obsidian 打开

```bash
# 直接用 Obsidian 打开这个文件夹作为 vault
obsidian "E:\LabNotes"
```

### 4. 命令行辅助工具

```bash
# 检查 wiki 健康状态
python scripts/wiki_tools.py lint

# 重建知识库总索引
python scripts/wiki_tools.py build-index --write

# 基于现有 wiki 做本地问答
python scripts/wiki_tools.py query "腹腔镜相机控制的核心方法是什么？"

# 把原始资料生成 source 页面
python scripts/wiki_tools.py ingest "raw/sources/papers_my_own/ocean-2026-04-14.pdf"
```

当前脚本支持：

- `lint`：检查 frontmatter 缺失、死链、孤立页、未 ingest 的原始资料、`[CONTRADICTION]` / `[OUTDATED]` 标记
- `build-index --write`：基于 `wiki/` 页面自动重建 `index.md`
- `query`：对本地 wiki 做轻量检索式问答，并输出引用页面与置信度
- `ingest`：读取 `md/txt/pdf` 原始资料，生成 `wiki/sources` 页面，并尝试同步更新日志与索引

---

## 🔧 工具链

| 工具 | 用途 |
|------|------|
| 本系统 (LLM) | 维护 wiki、ingest、query、lint |
| Obsidian | 可视化图谱、浏览、编辑 |
| Obsidian Web Clipper | 网页剪藏为 Markdown |
| VS Code | 代码/文本编辑（备选）|

---

## 🗂️ 归档与图谱

- 旧内容统一放在 `archive/legacy_notes/`
- Obsidian 图谱默认只看 `wiki/`，避免旧笔记干扰当前知识结构
- `archive/` 已加入排除规则，不参与搜索、图谱和未链接提及

---

## 🧱 数据库（Bases）怎么用

`知识库.base` 是 Obsidian 的 Bases 视图入口，可以把 `wiki/` 里的知识页按表格查看。

### 推荐用法

1. 在 Obsidian 里打开 `知识库.base`
2. 用表格看所有知识页的 `type / updated / tags / confidence`
3. 想只看某一类内容时，按 `type` 过滤，例如只看 `source` 或 `concept`
4. 想看最近更新，按 `updated` 排序

### 这和 raw/wiki/archive 的关系

- `raw/`：原始资料区，不当数据库改
- `wiki/`：真正的结构化知识区，最适合进 Bases
- `archive/`：旧内容归档，不参与当前知识图谱

---

## 📌 规则

1. **raw/ 不可修改**——LLM 只读，是知识源
2. **wiki/ 是 LLM 的输出**——不要手动大幅修改，由 LLM 维护
3. **矛盾不过夜**——发现立即标注 `[CONTRADICTION]`
4. **有价值就归档**——好的问答答案要写回 wiki

---

*基于 Andrej Karpathy 的 LLM Wiki 理念构建（2026）*
