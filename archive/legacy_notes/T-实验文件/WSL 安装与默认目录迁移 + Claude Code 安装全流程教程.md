---
date created: 星期日, 六月 15日 2025, 3:46:20 下午
date modified: 星期二, 七月 8日 2025, 2:12:56 下午
banner: "[[wallhaven-45vv71.webp]]"
words:
  2025-06-16: 1081
---

## WSL 安装与默认目录迁移 + Claude Code 安装全流程教程

本教程将指导你在 Windows 上完成 WSL（Windows Subsystem for Linux）的自动安装、迁移默认安装目录、以及在 WSL 中安装 Claude Code 的完整步骤。

---

### **一、自动安装 WSL（适用于 Win10/11 最新版）**

1. **以管理员身份打开 PowerShell**
    - 在“开始”菜单搜索“PowerShell”，右键以管理员身份运行。
2. **执行自动安装命令**

```powershell
wsl --install
```

    - 该命令会自动启用 WSL 所需的所有功能，并默认安装 Ubuntu 发行版。
    - 安装完成后，重启电脑。
3. **首次启动 Ubuntu**
    - 在“开始”菜单找到“Ubuntu”，首次启动会提示你设置 Linux 用户名和密码。

---

### **二、迁移 WSL 默认安装目录（如需将 WSL 安装到 D 盘等指定路径）**

默认情况下，WSL 的根文件系统会安装在 C 盘用户目录下。如果你想迁移到 D 盘等其他路径，可按如下操作：

在WSL终端（即Ubuntu终端）中输入以下命令：lsb_release -a
Ubuntu 24.04.2 LTS
1. **导出当前 WSL 发行版为 tar 包**

```powershell
wsl --export Ubuntu G:\WSL\wsl-ubuntu24.04.tar
```

2. **注销当前 WSL 发行版**

```powershell
wsl --unregister Ubuntu
```

3. **在目标目录重新导入 WSL 发行版**

```powershell
wsl --import Ubuntu G:\WSL\wsl-ubuntu20.04 G:\WSL\wsl-ubuntu24.04.tar
```

    - 这样，WSL 的根文件系统就会迁移到 G:\WSL\wsl-ubuntu20.04 。
    - 你可以修改路径为你想要的其他盘符和目录。
4. **启动迁移后的 WSL**
    - 在 PowerShell 输入 `wsl -d Ubuntu` 启动即可。

---

### **三、WSL 内部环境准备（Node.js、npm 安装）**

1. **进入 WSL 终端**
    - 在 Windows Terminal 或 PowerShell 输入 `wsl` 回车，或直接打开 Ubuntu 应用。
2. **更新软件源并升级系统**

```bash
sudo apt update
sudo apt upgrade
```

3. **安装 Node.js 和 npm**

```bash
sudo apt install nodejs npm
```

    - 安装完成后，检查版本：

```bash
node --version
npm --version
```

    - Claude Code 推荐 Node.js 18 及以上版本。如需更高版本，可参考 NodeSource 官方文档或使用 nvm 安装[^1_8][^1_9][^1_10]。

---

### **四、安装 Claude Code**

1. **全局安装 Claude Code**

```bash
npm install -g @anthropic-ai/claude-code
```

    - 如遇 WSL npm 识别为 Windows 平台导致安装失败，可先执行：

```bash
npm config set os linux
```

    - 或使用强制安装命令：

```bash
npm install -g @anthropic-ai/claude-code --force --no-os-check
```

    - 不要加 `sudo`[^1_10][^1_9][^1_6]。
2. **（可选）配置 npm 全局安装目录**
    - 避免权限问题，可设置全局前缀：

```bash
npm config set prefix ~/.npm-global
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

3. **进入你的项目目录**

```bash
cd /mnt/c/your/project/path
# 或在 WSL 内部的 Linux 路径
```

4. **启动 Claude Code**

```bash
claude
```

    - 首次启动需根据提示完成 OAuth 认证，需拥有 Anthropic Console 账号并完成一次性授权。

---

### **五、在 VSCode 中使用 Claude Code（推荐）**

1. **安装 VSCode 的 Remote - WSL 插件**
    - 在 VSCode 扩展市场搜索“Remote - WSL”并安装。
2. **用 VSCode 打开 WSL 终端**
    - 在终端面板选择 WSL 终端（如 Ubuntu-24.04）。
    - 在 WSL 终端中输入 `claude` 启动 Claude Code。

---

### **六、常见问题与注意事项**

- Claude Code 仅能在 WSL（Linux 环境）下运行，不能直接在 Windows 命令行运行[^1_6][^1_10]。
- 安装 Node.js 建议使用官方源或 nvm，确保版本符合要求（18+）。
- 若遇到 npm 权限或平台识别问题，优先使用 `npm config set os linux` 或 `--force --no-os-check` 选项[^1_10]。
- 迁移 WSL 目录后，原有数据会被清空，请提前做好备份。

---

## **参考命令汇总**

```powershell
# 自动安装 WSL
wsl --install

# 查看已安装 WSL 发行版
wsl --list --verbose

# 导出当前发行版
wsl --export Ubuntu D:\wsl-ubuntu20.04.tar

# 注销当前发行版
wsl --unregister Ubuntu

# 导入到指定目录
wsl --import Ubuntu D:\wsl-ubuntu20.04 D:\wsl-ubuntu20.04.tar
```

```bash
# 进入 WSL
wsl

# 更新系统
sudo apt update && sudo apt upgrade

# 安装 Node.js 和 npm
sudo apt install nodejs npm

# （可选）设置 npm 前缀
npm config set prefix ~/.npm-global
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# 配置 npm 平台
npm config set os linux

# 全局安装 Claude Code
npm install -g @anthropic-ai/claude-code --force --no-os-check

# 启动 Claude Code
claude
```


---

按照以上步骤，你即可在自定义目录下安装 WSL，并在 WSL 内部顺利安装和使用 Claude Code。