# AGENTS.md — LLM Wiki 维护规范

> 这是你的第二大脑维护手册。LLM 按此规范维护 wiki，你自己负责 sourcing、问正确的问题、复盘。

---

## 🎯 核心理念

- **知识是复合增长的**——每次 ingest/query/lint 都在让 wiki 变得更丰富、更准确
- **LLM 是知识库管理员，你是大脑本人**——LLM 负责整理、关联、记账；你负责判断、探索、提问
- **错误不过夜**——发现矛盾/过时信息立即标记、清理
- **复盘才有进步**——定期回顾知识库的完整性和正确性

---

## 🧠 关于我（第二大脑主人）

> 每次新 session 开始，LLM 先读这个，了解主人背景，后续 ingest 和 query 都基于此展开

- **姓名/昵称：**
- **背景：**
- **专业/领域：**
- **核心兴趣：**
- **当前目标/项目：**
- **知识边界（已熟悉/正在学/待探索）：**

> 例：
> - 姓名：你的名字
> - 背景：物联网方向研究者，关注 AI + 机器人
> - 核心兴趣：LLM 应用、知识管理、机器人控制
> - 当前目标：构建个人知识库，实现第二大脑
> - 知识边界：RAG 有基础了解，长上下文 LLM 是新学领域

---

## 📁 Wiki 结构约定

### 目录规范

```
wiki/
├── entities/          # 实体页：具体的人、物品、地点、事件
├── concepts/           # 概念页：抽象主题、理论、方法论
├── sources/            # 资料摘要页：每份原始资料对应一个摘要
├── comparisons/        # 对比分析页：对比两个以上概念/实体
├── synthesis/         # 综合分析页：跨多资料的高级总结
├── retrospectives/     # 复盘页：知识库健康回顾
└── misc/              # 其他：FAQ、待整理页等

raw/
├── sources/           # 原始资料（LLM 只读不修改）
└── assets/            # 图片、附件
```

### 命名规范

| 类型 | 格式 | 例 |
|------|------|-----|
| 实体页 | `entity-[简短英文名].md` | `entity-karpathy.md` |
| 概念页 | `concept-[简短英文名].md` | `concept-rag.md` |
| 资料摘要 | `source-[日期]-[简短名].md` | `source-2026-04-12-llm-wiki.md` |
| 对比页 | `compare-[A]-vs-[B].md` | `compare-rag-vs-llm-wiki.md` |
| 综合页 | `synthesis-[主题].md` | `synthesis-personal-km.md` |
| 复盘页 | `retro-[日期].md` | `retro-2026-04-weekly.md` |

### Frontmatter 元数据格式

```yaml
---
title: 页面标题
type: entity | concept | source | comparison | synthesis | retrospective
created: 2026-04-12
updated: 2026-04-12
tags: [tag1, tag2]
related:  # 关联页面（手动维护的交叉引用）
  - entity-karpathy
  - concept-rag
confidence: high | medium | low  # 信息可信度
source-ref:  # 仅 source 类型需要
  - raw/sources/example.md
aliases: [别名1, 别名2]  # 不同叫法，方便搜索
---

# 页面正文
```

---

## ⚙️ 三大核心操作

### 1️⃣ Ingest（摄入新资料）

**触发：** 你往 `raw/sources/` 放入新资料，并告诉我"帮我 ingest 这个"

**工作流：**

1. **读取原始资料**——完整读 raw/sources/ 下的文件
2. **理解消化**——与用户讨论关键要点、值得关注的细节
3. **写 source 摘要页**——在 `wiki/sources/` 生成资料摘要页
4. **更新相关实体/概念页**——检查是否涉及已有实体/概念，更新或新建
5. **更新 index.md**——在总索引中加入新页面条目
6. **追加 log.md**——记录本次 ingest 的时间、内容、关键决策
7. **检查矛盾**——发现新旧信息矛盾时，立即在相关页面标注 `[CONTRADICTION]` 并在复盘页记录

**Ingest Prompt 模板（LLM 内部使用）：**

```
你是一个知识库管理员。请处理以下资料：

## 原始资料
{full_content}

## 已有实体/概念（相关）
{existing_related_pages}

## 你的任务
1. 写一份 source 摘要页（500字内）
2. 识别其中涉及的关键实体，更新或创建实体页
3. 识别其中涉及的关键概念，更新或创建概念页
4. 检查是否与已有知识矛盾，如有则在相关页面标注 [CONTRADICTION]
5. 更新 index.md
6. 追加 log.md

## 输出格式
按 Frontmatter 格式输出各页面内容。
```

**质量要求：**
- 每份资料生成 1 个 source 页 + 更新 3-10 个实体/概念页
- 实体页要建立双向链接关系
- 新旧矛盾要在页内明确标注

---

### 2️⃣ Query（问答）

**触发：** 你问任何关于知识库内容的问题

**工作流：**

1. **读 index.md**——找到相关页面
2. **读相关页面**——理解上下文
3. **综合回答**——带引用溯源，有分歧要说明
4. **判断价值**——如果这个回答有价值，主动问用户"要不要归档到 wiki？"
5. **归档**——用户确认后，写入 synthesis/ 或 comparisons/，更新 index.md 和 log.md

**Query 回答格式：**

```
## 回答：{问题}

### 回答内容
{综合多个资料的回答}

### 引用溯源
- [{页面标题}](wiki/{filename}.md) — 关联原因
- [{页面标题}](wiki/{filename}.md) — 关联原因

### 置信度
{高/中/低，以及原因}

---
💡 这个回答有价值，我建议归档到 wiki。要我执行吗？
```

---

### 3️⃣ Lint（健康检查 & 错误清理）

**触发：** 你说"lint 一下"或"检查知识库健康"

**检查内容：**

- `[CONTRADICTION]` 标记的矛盾——解决或明确
- 过时信息——资料日期早于现有知识，标注或更新
- 孤立页面——没有任何交叉引用的页面
- 缺失链接——被引用但没有自己页面的概念
- 数据空白——某个重要主题完全没有覆盖
- 死链——引用了不存在的页面

**输出格式：**

```
## Lint 报告 — {日期}

### 🔴 需要立即处理
- 矛盾：{描述} → {建议处理方式}
- 过时：{页面} 中的 "{旧内容}" 被 "{新内容}" 替代

### 🟡 可以优化
- 孤立页面：{列表}
- 缺失链接：{被引用但无页面的概念}

### 🟢 健康
- {正常页面的数量} 个页面结构正常

---
建议优先处理红色项目。
```

---

## 🔄 复盘机制

### 周复盘（每周一次）

你说"这周复盘一下"，我执行：

1. **读 log.md**——回顾本周的 ingest 和 query
2. **Lint 扫描**——全库健康检查
3. **知识缺口分析**——哪些重要主题没有覆盖
4. **生成复盘页**——`wiki/retrospectives/retro-YYYY-WXX.md`

### 月复盘（每月一次）

你说"本月复盘"，我执行：

1. **全库审视**——按类别过一遍所有页面
2. **主题收敛**——相似页面合并，过时内容清理
3. **知识图谱审视**——检查实体间的关联是否合理
4. **生成月复盘页**

---

## 🔗 Obsidian 集成

Obsidian 是本系统的可视化前端，所有文件格式已兼容 Obsidian。

**Obsidian 专用约定：**

- **双向链接**：`[[页面名]]` 格式，LLM 生成页面时使用
- **标签**：`#tag` 格式，在 Frontmatter 和正文中均可使用
- **Graph View**：所有 wiki/ 下的 .md 文件自动出现在 Obsidian 图谱中
- **书签**：重要页面可用 Obsidian 书签功能标记

**建议的 Obsidian 设置：**

1. 打开 `D:\karpathy-knowledge-base\` 作为 vault
2. 在 `Settings → Files & Links` 中设置：
   - Attachment folder path: `raw/assets/`
   - Default location: `wiki/${filename}/`
3. 启用 `Graph View` 插件查看知识图谱
4. 启用 `Backlinks` 插件查看页面引用

---

## 📊 NotebookLM 集成

NotebookLM 是 Google 的 AI 笔记本，适合作为替代前端。

**导入方式：**

1. Obsidian → 导出整个 `wiki/` 文件夹为 ZIP
2. 导入到 NotebookLM
3. 或：将 `raw/sources/` 的资料直接导入 NotebookLM

**反向同步（如果有新产出）：**

1. 在 NotebookLM 中生成笔记/摘要
2. 导出为 Markdown
3. 放入 `raw/sources/` → 触发 ingest

---

## 📋 index.md 格式

```markdown
# 知识库总索引

> 最后更新：2026-04-12 | 共 {N} 个页面

## 🧑 实体（{n} 个）
| 页面 | 摘要 | 标签 |
|------|------|------|
| [entity-xxx](wiki/entities/entity-xxx.md) | 一句话描述 | #tag |

## 📚 概念（{n} 个）
| 页面 | 摘要 | 标签 |
|------|------|------|
| [concept-xxx](wiki/concepts/concept-xxx.md) | 一句话描述 | #tag |

## 📄 资料（{n} 个）
| 页面 | 日期 | 关键要点 |
|------|------|----------|
| [source-xxx](wiki/sources/source-xxx.md) | 2026-04-12 | 要点1、要点2 |

## 🔄 复盘（{n} 个）
| 页面 | 日期 |
|------|------|
| [retro-xxx](wiki/retrospectives/retro-xxx.md) | 2026-04-12 |
```

---

## 📝 log.md 格式

```markdown
# 操作日志

> 格式：`## [日期] 操作类型 | 描述`

## [2026-04-12] ingest | 新文章：Karpathy LLM Wiki 解读
- 涉及实体：entity-karpathy, entity-andrej-karpathy
- 涉及概念：concept-llm-wiki, concept-rag, concept-ingest
- 矛盾标记：无
- 更新页面：index.md

## [2026-04-12] query | 问：Karpathy 方案和 RAG 的核心区别
- 回答归档：synthesis-karpathy-vs-rag.md
- 置信度：高

## [2026-04-12] lint | 周检
- 矛盾：0 个
- 孤立页面：2 个 → 已处理
- 建议：本周新增了 RAG 相关概念，建议补充 RAG 的优缺点对比页
```

---

## 🚨 错误处理约定

| 标记 | 含义 | 处理方式 |
|------|------|----------|
| `[CONTRADICTION]` | 新旧信息矛盾 | 页面内标注，两说并存，用户判断 |
| `[OUTDATED]` | 信息可能过时 | 保留旧内容，添加新内容，说明时间线 |
| `[UNCLEAR]` | 来源不明确 | 降低置信度，标注需核实 |
| `[GAP]` | 知识缺口 | 在复盘页记录，建议后续补充 |

---

## 💡 快速开始

1. **初始化个人 Profile**——告诉我你的背景，我来填写 PROFILE.md
2. **放入第一份资料**——放到 `raw/sources/`，说"帮我 ingest"
3. **开始问答**——问任何问题，我会从 wiki 回答，有价值的归档
4. **定期 lint**——说"lint 一下"让我检查健康状态
5. **复盘**——每周/每月说"复盘一下"

---

*此文件是动态规范，随使用经验迭代更新。*
