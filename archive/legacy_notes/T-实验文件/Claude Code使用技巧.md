---
date created: 星期日, 七月 20日 2025, 4:01:33 下午
date modified: 星期一, 七月 21日 2025, 10:56:13 上午
banner: "[[wallhaven-r7zm17.webp]]"
words:
  2025-07-20: 2892
---
```
Interactive Mode Commands:
 /add-dir - Add a new working directory
 /bug - Submit feedback about Claude Code
 /clear - Clear conversation history and free up context
 /compact - Clear conversation history but keep a summary in context. Optional: /compact [instructions for summarization]
 /config - Open config panel
 /cost - Show the total cost and duration of the current session
 /doctor - Diagnose and verify your Claude Code installation and settings
 /exit - Exit the REPL
 /export - Export the current conversation to a file or clipboard
 /help - Show help and available commands
 /hooks - Manage hook configurations for tool events
 /ide - Manage IDE integrations and show status
 /init - Initialize a new CLAUDE.md file with codebase documentation
 /install-github-app - Set up Claude GitHub Actions for a repository
 /login - Sign in with your Anthropic account
 /logout - Sign out from your Anthropic account
 /mcp - Manage MCP servers
 /memory - Edit Claude memory files
 /migrate-installer - Migrate from global npm installation to local installation
 /model - Set the AI model for Claude Code
 /permissions - Manage allow & deny tool permission rules
 /pr-comments - Get comments from a GitHub pull request
 /release-notes - View release notes
 /resume - Resume a conversation
 /review - Review a pull request
 /status - Show Claude Code status including version, model, account, API connectivity, and tool statuses
 /upgrade - Upgrade to Max for higher rate limits and more Opus
 /vim - Toggle between Vim and Normal editing modes
```
## 技巧一：创建CLAUDE.md项目配置文件【实用指数：10分】

这是Claude Code最重要的功能之一！CLAUDE.md就像是你项目的"说明书"，Claude会在每次对话开始时自动读取这个文件。

**具体操作：**

1. 在项目根目录创建`CLAUDE.md`文件
2. 记录项目的编码规范、常用命令、文件结构等
3. 使用`/init`命令可以让Claude自动生成初始模板
```# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Status

This is a new/empty repository. No existing codebase structure, build tools, or development commands have been detected.

## Development Setup

When files are added to this repository, update this document with:

- Build commands (e.g., `npm run build`, `make`, `cargo build`)
- Test commands (e.g., `npm test`, `pytest`, `go test`)
- Linting/formatting commands (e.g., `npm run lint`, `ruff check`)
- Development server commands (e.g., `npm run dev`, `cargo run`)

## Architecture Notes

As the codebase develops, document the high-level architecture here, including:

- Main entry points
- Key directories and their purposes
- Important patterns or conventions
- Database schema or data models (if applicable)
- API structure (if applicable)

## Important Commands

None yet - update this section as the project develops.
```

**标准化内容：**

- 项目结构说明
    
- 开发规范定义
    
- 常用命令记录
    
- 依赖关系说明

## 技巧二：掌握快捷命令与权限管理【实用指数：9分】

Claude Code提供了丰富的斜杠命令，掌握这些命令能大幅提升操作效率。

**核心命令清单：**

- `/help` - 查看所有可用命令
    
- `/clear` - 清除对话历史
    
- `/permissions` - 管理工具权限
    
- `/config` - 修改配置设置
    
- `/model` - 切换AI模型
    
- `/status` - 查看系统状态
    

**权限管理技巧：**

- 默认情况下，Claude会为每个操作请求权限
    
- 可以选择"始终允许"来避免重复确认
    
- 使用`/permissions add Edit`允许文件编辑权限
    

**新手建议：**刚开始不要着急跳过权限检查，先熟悉Claude的操作逻辑。

## 技巧三：激活深度思考模式【实用指数：8分】

当面临复杂问题时，你可以激活Claude的深度思考能力。

**思考级别：**

1. `think` - 基础思考
    
2. `think hard` - 深度思考
    
3. `think harder` - 更深度思考
    
4. `ultrathink` - 极限思考（最消耗token）
    

**使用场景：**

- 复杂算法设计
    
- 架构决策分析
    
- 性能优化方案
    
- 代码重构规划
    

**实用建议：**对于新手来说，在处理复杂逻辑时加上"think hard"，能让Claude给出更详细的解释和步骤分解。

## 技巧四：优化上下文管理与清理【实用指数：10分】

这是控制成本和提升效率的关键技巧！

**核心命令：**

- `/clear` - 完全清除对话历史，开始新对话
    
- `/compact` - 压缩对话历史，保留关键信息
    

**使用策略：**

- 频繁使用`/clear`比你想象的更重要
    
- 当话题切换时，立即清理上下文
    
- 长对话会让AI变得不可预测
    

**成本控制：**

- 每次对话都消耗token，及时清理能节省费用
    
- 根据实际测试，主动清理可节省30-50%的token消耗
    


## 技巧五：集成MCP服务器扩展功能【实用指数：9分】

MCP（Model Context Protocol）让Claude Code能够连接外部工具和服务。

**常用MCP服务器：**

- 文件系统服务器：`claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem`
    
- GitHub服务器：`claude mcp add github -- env GITHUB_TOKEN=your_token npx -y @modelcontextprotocol/server-github`
    
- 浏览器服务器：`claude mcp add puppeteer -- npx -y @modelcontextprotocol/server-puppeteer`
    

**实用场景：**

- 数据库查询和操作
    
- API接口调用
    
- 网页抓取和自动化
    
- 云服务集成
    

**新手入门：**先从文件系统服务器开始，它能让Claude直接操作你的项目文件。

## 技巧六：设置免授权模式【实用指数：7分】

当你需要进行批量操作时，频繁的权限确认会严重影响效率。

**启动命令：**

bash

`claude --dangerously-skip-permissions`

**便捷设置：**

bash

`# 设置别名，方便使用 alias yolo="claude --dangerously-skip-permissions"`

**⚠️ 安全提醒：**

- 仅在信任的环境和项目中使用
    
- 建议先备份重要文件
    
- 新手建议先熟悉正常模式再使用
    

## 技巧七：掌握终端快捷键技巧【实用指数：8分】

熟练的快捷键操作能显著提升使用体验。

**基础快捷键：**

- `Tab` - 命令自动补全
    
- `↑↓` - 浏览命令历史
    
- `ESC` - 中断AI操作
    
- `Option(Win是Alt键) + Enter` - 换行（需配置）
    
- 连续按下两次 `Ctrl + C` - 退出Claude code程序
    

**高级技巧：**

- 输入`/`快速查看所有斜杠命令
    
- 使用`\`后按Enter创建换行
    
- 双击ESC可以回到上一条消息并分叉对话
    

## 技巧八：Hook钩子工具【实用指数：9分】

Claude Code 的 **hook（钩子）工具**是一套非常强大的功能，允许开发者在 Claude Code 生命周期的关键节点（如工具调用前后、通知或终止响应时）自动执行自定义 Shell 脚本，实现流程自动化、安全控制、日志记录、团队规范等多种目的。这极大地提升了 AI 编程的可扩展性和确定性，为团队协作和合规带来极大便利

**步骤一：打开钩子设置**

- 输入 `/hooks` 命令，选择需要配置的事件，比如 `PreToolUse`。
    

**步骤二：添加钩子匹配器**

- 匹配器决定这个钩子是否生效（比如只对 Bash 工具、Read 工具生效），如：
    
    - Bash（仅对 Shell 命令）
        
    - Read|Grep（支持正则表达式，多个工具）
        
    - 留空代表所有工具通用。
        

**步骤三：添加钩子命令**

- 输入命令脚本。例如最常用的日志记录钩子：
    
    bash
    
    `jq -r '"\(.tool_input.command) - \(.tool_input.description // "No description")"' >> ~/.claude/bash-command-log.txt`
    
    该脚本自动记录被 Claude 运行的 Bash 指令和描述，保存到指定日志文件。
    

**步骤四：保存位置**

- 建议选“User settings”（~/.claude/settings.json），让钩子对所有项目生效。团队项目可放 .claude/settings.json，也支持本地或企业级策略配置。
    

**步骤五：验证钩子工作效果**

- 再次运行 `/hooks` 检查设置，或实际触发命令后检查生成的日志文件。`

## 技巧九：多实例并行开发【实用指数：7分】

对于大型项目，你可以同时运行多个Claude Code实例。

**并行场景：**

- 前端和后端同时开发
    
- 多个功能模块并行
    
- 代码编写和测试分离
    
- 不同分支的开发工作
    

**操作方法：**

1. 在不同终端窗口启动Claude
    
2. 使用Git worktrees创建独立工作目录
    
3. 每个实例处理不同的任务
    

**效率提升：**可以让一个Claude写代码，另一个做代码审查，分工协作效率更高。

## 技巧十：AI代理任务分工【实用指数：8分】

使用Task工具可以创建专业角色分工，处理复杂项目。

**Task工具用法：**

text

`> 使用4个不同角色的子任务分析这个系统架构：   1. 系统架构师视角  2. 安全专家视角  3. 性能优化专家视角  4. 用户体验专家视角`

**优势特点：**

- 并行处理，节省时间
    
- 多角度分析，更全面
    
- 独立上下文，避免混淆
    
- 专业视角，质量更高
    

**实际应用：**特别适合技术选型、架构设计、代码审查等需要多维度分析的任务。

## 实用性总结

从我们的数据分析可以看出，这十大技巧中有两个获得了满分10分的最高实用性评价：CLAUDE.md项目配置文件和上下文管理与清理。这说明项目标准化和成本控制是Claude Code使用中最重要的两个方面。

对于开发者新手，我建议按以下优先级来学习：

1. **必掌握**（实用指数10分）：CLAUDE.md配置文件、上下文管理
    
2. **优先学习**（实用指数9分）：快捷命令、MCP集成、项目初始化
    
3. **进阶技巧**（实用指数8分）：深度思考模式、快捷键操作、AI任务分工
    
4. **特殊场景**（实用指数7分）：免授权模式、多实例并行
    
