---
banner: "![[E-功能插件/pixel-banner-images/wallhaven-45vv71.webp]]"
content-start: 101
---
```widgets
type: clock
format: "12hr" | "24hr"
```
## 【什么是Codex CLI】
Codex CLI是OpenAI推出的开源命令行工具，它具备以下特点：
- 轻量级设计，直接在你的终端运行
- 支持自然语言交互，像和ChatGPT聊天一样编程
- 可以读取、修改、运行你的代码
- 支持多种编程语言和框架
- 完全本地化，保护你的代码隐私

## 【系统要求检查】
在开始安装之前，我们先检查一下系统要求：

**画面提示：** 显示系统要求列表

你需要确保你的电脑满足以下条件：
1. **Node.js**：22版本或更高
2. **网络**：需要能访问OpenAI的服务
3. **Git**（可选但推荐）：用于版本控制

**画面提示：** 在桌面上打开命令提示符演示检查

现在让我检查一下我的系统。打开PowerShell，输入：
```
node -v
npm -v
```

如果显示了版本号，说明Node.js已经安装。如果没有，我们接下来就安装它。

---

## 【第一步：安装Node.js】

**画面提示：** 打开浏览器，访问nodejs.org

首先，我们需要安装Node.js。打开浏览器，访问 nodejs.org

**操作步骤：**
1. 点击"Download Node.js (LTS)"下载LTS版本
2. 选择Windows版本的.msi安装包
3. 下载完成后，双击安装包
4. 安装向导中保持默认设置，一路点击"Next"
5. 确保勾选"Add to PATH"选项
6. 点击"Install"开始安装

**画面提示：** 实际演示整个安装过程

安装完成后，我们重新打开PowerShell验证安装：
```
node -v
npm -v
```

看到版本号就说明安装成功了！

---

## 【第二步：安装Codex CLI】（4:00-5:30）

现在我们来安装Codex CLI本体。在PowerShell中输入：

```
npm install -g @openai/codex
```

**画面提示：** 显示安装过程，包括下载进度

这个命令会全局安装Codex CLI，可能需要几分钟时间，请耐心等待。

安装完成后，我们验证一下是否成功：
```
codex --version
```

**如果遇到权限问题：**
- 以管理员身份运行PowerShell
- 或者使用：`npm install -g @openai/codex --force`

**画面提示：** 显示可能的错误信息和解决方案

如果看到版本号，恭喜你，Codex CLI已经成功安装！

---

## 【第三步：配置API密钥】

要使用Codex CLI，你需要一个OpenAI账号。这里有两种方式：

**方式一：使用ChatGPT登录（推荐新手）**

直接运行：
```
codex
```

选择"Sign in with ChatGPT"，系统会打开浏览器让你登录。

**画面提示：** 演示登录过程

**方式二：使用API密钥**

如果你有OpenAI API密钥，可以设置环境变量：

**临时设置（仅当前会话有效）：**
```
$env:OPENAI_API_KEY = "your-api-key-here"
```

**永久设置：**
```
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY","your-api-key-here","User")
```

**画面提示：** 显示如何获取API密钥（访问platform.openai.com）

记得把"your-api-key-here"替换成你的真实API密钥。

---

## 【第四步：Windows特有问题解决】（7:00-8:30）

在Windows上使用Codex CLI可能会遇到一些特有问题，我们来逐一解决：

**问题1：找不到sh.exe**
如果遇到"sh.exe not found"错误，你需要安装Git：

**画面提示：** 访问git-scm.com

1. 访问 git-scm.com 下载Git
2. 安装时选择"Use Git and optional Unix tools from the Command Prompt"
3. 重启PowerShell

**问题2：沙盒功能不可用**
Windows上的沙盒功能是实验性的，如果遇到问题：
- 使用建议模式而不是全自动模式
- 或者考虑在WSL2中运行

**问题3：Python依赖问题**
某些功能需要Python支持：
1. 从Microsoft Store安装Python 3.13
2. 或从python.org下载并安装

**画面提示：** 演示安装Python的过程

---

## 【第五步：首次运行和基本使用】

现在让我们来第一次运行Codex CLI：

```
codex
```

**画面提示：** 显示Codex CLI的启动界面

你会看到一个交互式界面，这里你可以：
- 用自然语言描述你想要的功能
- 让AI分析现有代码
- 生成新的项目

**演示案例1：生成一个简单的HTML页面**

我输入：
```
创建一个简单的个人介绍网页，包含姓名、职业和联系方式
```

**画面提示：** 显示AI生成代码的过程和结果

**演示案例2：代码解释**

我输入：
```
解释这个JavaScript函数是做什么的
```

然后提供一段代码让AI分析。

**画面提示：** 显示AI解释代码的过程

**审批模式说明：**
Codex CLI有三种模式：
- **建议模式**：AI提供建议，你来决定是否执行
- **自动编辑模式**：AI可以直接修改文件，但运行命令前会询问
- **全自动模式**：在沙盒环境中完全自动执行

你可以用这些命令切换：
```
codex --auto-edit
codex --full-auto
```

---

## 【常见问题和故障排除】

在使用过程中，你可能会遇到以下问题：

**问题1："codex命令找不到"**
- 检查npm全局路径是否在PATH中
- 重启PowerShell或重启电脑
- 使用`npm config get prefix`查看npm路径

**问题2："网络连接错误"**
- 检查网络连接
- 确认能访问OpenAI服务
- 如果在公司网络，可能需要配置代理

**问题3："API配额不足"**
- 检查你的OpenAI账户余额
- ChatGPT Plus用户有免费额度
- 考虑升级到Pro账户获得更多使用量

**画面提示：** 显示解决这些问题的具体步骤

如果还是有问题，可以：
- 查看官方文档：github.com/openai/codex
- 在GitHub Issues中搜索相似问题
- 或者在评论区留言，我会尽力帮助大家

---

## 【结尾总结】

好了，今天的教程就到这里。让我们快速回顾一下安装步骤：

1. **安装Node.js 22+版本**
2. **运行`npm install -g @openai/codex`安装CLI**
3. **配置OpenAI账号或API密钥**
4. **解决Windows特有问题（如Git、Python依赖）**
5. **运行`codex`开始使用**

**画面提示：** 显示完整的命令列表

Codex CLI是一个非常强大的开发工具，它能显著提高我们的编程效率。无论你是新手还是经验丰富的开发者，都能从中受益。

如果这个视频对你有帮助，记得点赞、收藏、关注三连！有任何问题欢迎在评论区讨论。

下期视频我们将深入介绍Codex CLI的高级功能和实战案例，敬请期待！

我们下期见，拜拜！

---
![[Pasted image 20250907172104.png]]