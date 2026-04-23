---
date created: 星期日, 七月 27日 2025, 2:20:17 下午
date modified: 星期一, 七月 28日 2025, 9:31:44 上午
banner: "[[wallhaven-45vv71.webp]]"
---
## 什么是Sub Agents？核心概念解析

### 专业化智能助手的诞生

Sub Agents（子智能体）本质上是**预配置的专业AI助手**，每个都有自己的专长领域和独立的工作环境[^1]。与传统的通用AI助手不同，Sub Agents采用了"术业有专攻"的设计理念，让每个智能体都专注于特定的任务领域。

当业领域的任务时，会自动将任务委托给相应的专业Sub Agent处理，从而获得更精准、更专业的结果[^1]。

### Sub Agents的四大核心特征

**独立上下文窗口**：每个Sub Agent都在独立的沙盒环境中运行，拥有完全独立的上下文窗口，有效防止不同任务间的信息污染[^1]。

**专业化系统提示词**：每个Sub Agent都配备了针对特定领域优化的系统提示词，确保在专业领域内的高效表现[^1]。

**灵活的工具权限**：可以为每个Sub Agent配置不同的工具访问权限，既保证功能需求，又维护系统安全[^1]。

**跨项目重用**：创建好的Sub Agents可以跨项目使用，并支持团队共享，实现一致性的工作流程[^2]。

## Sub Agents的创建和管理

### 快速创建流程

创建Sub Agent的过程非常简单：

**1. 打开Sub Agents界面**
在VS Code中使用快捷键 `Cmd + Esc`（Mac）打开Claude Code，然后输入 `/agents`[^2]。

**2. 选择创建模式**

- 选择"Create New Agent"
- 决定是创建项目级还是用户级Sub Agent

**3. 定义Sub Agent**
Anthropic建议首先使用Claude生成初始的Sub Agent，然后根据具体需求进行定制[^4]：

- 详细描述Sub Agent的功能和使用场景
- 选择需要授权的工具（或留空继承所有工具）
- 系统会显示所有可用工具，方便选择

**4. 保存和使用**
Sub Agent创建完成后即可使用，Claude会在适当时候自动调用，也可以明确指定：

```
> 使用code-reviewer sub agent检查我最近的更改
```


### 文件存储结构

Sub Agents以Markdown文件形式存储，支持两种位置：

- **项目级**：`.claude/agents/` 目录（优先级最高）
- **用户级**：`~/.claude/agents/` 目录（跨项目使用）[^1]


## Sub Agents的革命性优势

### 专业化分工提升效率

传统的AI编程助手往往是"万金油"式的通用工具，而Sub Agents则实现了真正的专业化分工。就像现实中的开发团队一样，不同的专家负责不同的任务：

- **代码审查专家**：专门负责代码质量检查、安全漏洞识别
- **调试专家**：专注于错误排查、性能问题诊断
- **架构师**：负责系统设计、技术选型
- **测试工程师**：专门编写和执行测试用例

这种专业化分工带来的效率提升是显而易见的[^2]。

### 上下文隔离防止污染

每个Sub Agent都有自己独立的上下文窗口，这意味着：

- 代码审查任务不会被调试信息干扰
- 数据分析工作不会被架构设计讨论影响
- 每个任务都能获得最纯净、最专注的处理环境[^1]


### 团队协作标准化

Sub Agents支持跨项目共享和版本控制，这为团队协作带来了新的可能性：

- **统一的代码审查标准**：整个团队使用相同的代码审查Sub Agent
- **一致的调试流程**：标准化的问题排查方法
- **共享的最佳实践**：将经验沉淀到Sub Agent中供团队复用[^1]


## 实战案例一：代码审查Sub Agent

让我们通过一个具体的代码审查场景来展示Sub Agents的威力。

### 创建代码审查专家

首先，我们创建一个专门负责代码审查的Sub Agent：

```markdown
---
name: code-reviewer
description: 专业代码审查专家，主动审查代码质量、安全性和可维护性
tools: Read, Grep, Glob, Bash
---

你是一位资深的代码审查专家，确保代码的高质量和安全性。

当被调用时：
1. 运行git diff查看最近的更改
2. 专注于修改的文件
3. 立即开始审查

审查清单：
- 代码简洁易读
- 函数和变量命名清晰
- 无重复代码
- 适当的错误处理
- 无暴露的密钥或API密码
- 输入验证完善
- 良好的测试覆盖率
- 性能考虑

按优先级提供反馈：
- 关键问题（必须修复）
- 警告（应该修复）
- 建议（考虑改进）
```


### 实际使用效果

当我们输入"用code reviewer分析当前项目的代码"时，这个专业的Sub Agent会：

1. **自动运行git diff**查看最近的代码变更
2. **深入分析代码质量**，检查命名规范、逻辑结构
3. **识别安全隐患**，查找潜在的安全漏洞
4. **提供改进建议**，给出具体的优化方案[^3]

整个过程完全自动化，而且分析结果专业且详细，就像有一位资深工程师在为你进行代码审查。

## 实战案例二：构建Spec-Driven开发工作流

### 复现Amazon Kiro的开发模式

Claude Code的Sub Agents功能让我们能够复现Amazon Kiro的Spec-Driven AI编程方式[^2]。这种开发模式强调规范驱动，告别传统的"Vibe Coding"（凭感觉编程）。

### 三个专业化Agent的协作

为了实现完整的Spec-Driven工作流，我们需要创建三个专业化的Sub Agents：

**1. 项目指导架构师**

- 角色：AI项目分析师和文档架构师
- 职责：分析项目需求，创建基础文档框架
- 输出：项目规格文件、技术栈说明

**2. 专家级软件架构师**

- 角色：协作规划师
- 职责：项目整体规划和架构设计
- 输出：功能需求文档、架构设计文件

**3. 执行导向软件工程师**

- 角色：任务执行专家
- 职责：严格按照规范实现功能
- 输出：实际可运行的代码[^2]


### To-Do List应用完整开发流程

让我们通过一个To-Do List应用的开发来展示这三个Agent的协作：

**第一阶段：项目初始化**
项目指导架构师创建项目的指导文件，包括：

- 项目结构说明
- 技术栈选择
- 开发规范定义

**第二阶段：功能规划**
专家级软件架构师规划To-Do List的功能：

- 任务添加和删除
- 优先级设置
- 状态管理
- 用户界面设计

**第三阶段：代码实现**
执行导向软件工程师根据规划文件：

- 严格按照架构设计实现代码
- 确保代码符合预定规范
- 实现所有计划功能[^2]

通过这种分工协作，最终我们可以在浏览器中看到一个功能完整的To-Do List应用，包括添加任务、设定优先级、标记完成、编辑和删除等功能。

## 实战案例三：数据分析专家Sub Agent

### 专业化数据处理

假设我们需要创建一个专门处理数据分析任务的Sub Agent：

```markdown
---
name: data-scientist
description: 数据分析专家，处理SQL查询、BigQuery操作和数据洞察
tools: Bash, Read, Write
---

你是一位数据科学家，专门从事SQL和BigQuery分析。

当被调用时：
1. 理解数据分析需求
2. 编写高效的SQL查询
3. 适当时使用BigQuery命令行工具
4. 分析和总结结果
5. 清晰地展示发现

关键实践：
- 编写带有适当过滤器的优化SQL查询
- 使用适当的聚合和连接
- 包含解释复杂逻辑的注释
- 格式化结果以提高可读性
- 提供数据驱动的建议
```

这个专业的数据分析Sub Agent能够：

- **自动优化SQL查询**，提高执行效率
- **生成数据可视化**，让结果更直观
- **提供专业洞察**，发现数据背后的规律
- **成本控制**，确保查询的成本效益[^1]




### 最佳实践建议

**从Claude生成开始**：建议先让Claude生成初始的Sub Agent，然后根据需求定制，这样既保证基础功能完整，又能满足个性化需求[^1]。

**专注单一职责**：创建专注于单一明确职责的Sub Agent，而不是试图让一个Sub Agent处理所有事情[^1]。

**详细的系统提示词**：在系统提示词中包含具体的指令、示例和约束条件，提供的指导越详细，Sub Agent的表现越好[^1]。

**限制工具访问**：只授予Sub Agent完成任务所必需的工具，这既提高了安全性，也帮助Sub Agent专注于相关操作[^1]。

**版本控制管理**：将项目级Sub Agent纳入版本控制，让团队能够共同受益并协作改进[^1]。

## 高级使用技巧

### Sub Agent链式调用

对于复杂的工作流，可以链式使用多个Sub Agents：

```
> 首先使用code-analyzer sub agent找出性能问题，然后使用optimizer sub agent修复它们
```

这种链式调用让复杂任务的处理变得更加系统化和专业化[^1]。

### 并行任务处理

Claude Code支持最多10个Sub Agent并行工作，这对于大型项目非常有用：

```
> 使用4个任务并行探索代码库。每个agent应该探索不同的目录。
```

每个Sub Agent都有自己的上下文窗口，这是一种巧妙的方式来为大型代码库获得额外的上下文窗口[^5]。

### 动态Agent选择

Claude Code会根据上下文智能选择Sub Agents。为了获得最佳效果，要让`description`字段具体且面向行动：

- 使用"主动使用"、"必须使用"等关键词
- 明确描述使用场景和触发条件
- 提供具体的任务边界[^1]

## Sub Agent示例
- **代码审查员**
```
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is simple and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage
- Performance considerations addressed

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.
```

- **Debugger**
```
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

Debugging process:
- Analyze error messages and logs
- Check recent code changes
- Form and test hypotheses
- Add strategic debug logging
- Inspect variable states

For each issue, provide:
- Root cause explanation
- Evidence supporting the diagnosis
- Specific code fix
- Testing approach
- Prevention recommendations

Focus on fixing the underlying issue, not just symptoms.
```

- **数据分析师**
```
---
name: data-scientist
description: Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries.
tools: Bash, Read, Write
---

You are a data scientist specializing in SQL and BigQuery analysis.

When invoked:
1. Understand the data analysis requirement
2. Write efficient SQL queries
3. Use BigQuery command line tools (bq) when appropriate
4. Analyze and summarize results
5. Present findings clearly

Key practices:
- Write optimized SQL queries with proper filters
- Use appropriate aggregations and joins
- Include comments explaining complex logic
- Format results for readability
- Provide data-driven recommendations

For each analysis:
- Explain the query approach
- Document any assumptions
- Highlight key findings
- Suggest next steps based on data

Always ensure queries are efficient and cost-effective.
```