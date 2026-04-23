---
start date: 2025-02-16
banner: "[[wallhaven-45vv71.webp]]"
date created: 星期日, 一月 26日 2025, 3:15:27 下午
date modified: 星期一, 七月 14日 2025, 9:22:51 上午
autoscroll-speed: 12
words:
  2025-02-17: 526
  2025-03-13: 528
  2025-03-16: 554
  2025-03-18: 809
  2025-03-31: 280
  2025-04-06: 355
  2025-04-08: 0
  2025-04-13: 32
  2025-07-01: 1682
  2025-07-06: 1908
  2025-07-13: 2556
  2025-07-14: 878
---
# 通过Kimi K2 API配置并驱动Claude Code

**1. 环境准备**
- Claude Code 官方目前原生支持Windows。
- 安装并配置好Git for Windows，确保 Node. js 环境可用。

**2. 安装 Claude Code**

在 终端中执行：`npm install -g @anthropic-ai/claude-code`

安装完成后可通过 `claude --version` 验证。

**3. 获取 Kimi K2 API Key**

- 前往 Moonshot/Kimi 官方平台，注册账号并在用户中心申请 API Key。

**4. 配置环境变量**

Claude Code 通过环境变量来指定 API Key 和请求地址。具体操作如下：
Linux跟Mac：
```
export ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic/  
export ANTHROPIC_API_KEY=YOUR_API_KEY_HERE
```

Windows powershell:
```
$env:ANTHROPIC_BASE_URL = "https://api.moonshot.ai/anthropic/"
$env:ANTHROPIC_API_KEY = "YOUR_API_KEY_HERE"
claude
```

- 注意：国内账号可能需要用 `https://api.moonshot.cn/anthropic` 作为 BASE_URL，具体以官方文档为准。注意目前每次进入新命令行都要输一次环境变量。如想避免这点，后续可以加入到命令行启动加载的配置文件。

**5. 启动 Claude Code**

在终端输入：`claude`

首次启动会提示是否使用你配置的 API Key，选择 yes 并信任当前目录即可。

---

# Claude Code 重大更新-原生支持Windows系统
## 1.0.51
- Added support for native Windows (requires Git for Windows)  
    添加了对本机 Windows 的支持（需要适用于 Windows 的 Git）
- Added support for Bedrock API keys through environment variable AWS_BEARER_TOKEN_BEDROCK  
    通过环境变量 AWS_BEARER_TOKEN_BEDROCK 添加了对 Bedrock API 密钥的支持
- Settings: /doctor can now help you identify and fix invalid setting files  
    设置：/doctor 现在可以帮助您识别和修复无效的设置文件
- `--append-system-prompt` can now be used in interactive mode, not just --print/-p.  
    `--append-system-prompt` 现在可以在交互模式下使用，而不仅仅是 --print/-p。
- Increased auto-compact warning threshold from 60% to 80%  
    将自动压缩警告阈值从 60% 提高到 80%
- Fixed an issue with handling user directories with spaces for shell snapshots  
    修复了处理带有 shell 快照的带空格的用户目录的问题
- OTEL resource now includes os.type, os.version, host.arch, and wsl.version (if running on Windows Subsystem for Linux)  
    OTEL 资源现在包括 os.type、os.version、host.arch 和 wsl.version（如果在适用于 Linux 的 Windows 子系统上运行）
- Custom slash commands: Fixed user-level commands in subdirectories  
    自定义斜杠命令：修复了子目录中的用户级命令
- Plan mode: Fixed issue where rejected plan from sub-task would get discarded  
    计划模式：修复了子任务中被拒绝的计划被丢弃的问题

To install Claude Code, run the following command:
```
npm install -g @anthropic-ai/claude-code
```

After the installation process completes, navigate to your project and start Claude Code:
```
cd ‘E:\Cursor\zotero-one’
```



---


## 免费领取 Claude Code 100美元的API使用量
无需信用卡，无需付费，立即体验Claude Code AI 编程助手

## 注册流程
用这个网址注册之后就得100刀账户余额，需要用github，没有就先注册一个。
```
https://anyrouter.top/register?aff=toOC
```

## 一键开始使用
### ⚡ 三步快速开始

**1. 注册获取令牌** → [AnyRouter](https://anyrouter.top/) 注册后获取 API 令牌

**2. 安装 Claude Code** →Win系统 `看我之前的视频` Mac系统 `npm install -g @anthropic-ai/claude-code`

**3. 复制粘贴启动** → 复制下方命令到终端即可使用
```
export ANTHROPIC_AUTH_TOKEN=YOUR_API_KEY_HERE
export ANTHROPIC_BASE_URL=https://anyrouter.top
claude
```
### 持久化配置环境变量（可选）
```
echo -e '\n export ANTHROPIC_AUTH_TOKEN=sk-...' >> ~/.bash_profile  
echo -e '\n export ANTHROPIC_BASE_URL=https://anyrouter.top' >> ~/.bash_profile  
echo -e '\n export ANTHROPIC_AUTH_TOKEN=sk-...' >> ~/.bashrc  
echo -e '\n export ANTHROPIC_BASE_URL=https://anyrouter.top' >> ~/.bashrc
```

