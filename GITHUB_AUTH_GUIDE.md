# 🔐 GitHub 身份验证配置指南

## ⚠️ 当前状态

**已完成：**
- ✅ 远程仓库已添加：`https://github.com/du118/wechat-bot.git`
- ⚠️ 需要配置身份验证

**问题：**
推送代码时需要 GitHub 用户名和密码（或 Personal Access Token）。

---

## 🔧 解决方案（3种方法）

### 方法1：使用 Personal Access Token（推荐）

#### 步骤1：创建 Personal Access Token

1. **访问 GitHub Settings**
   - 访问：https://github.com/settings/tokens
   - 登录你的 GitHub 账号

2. **生成新 Token**
   - 点击 **"Generate new token (classic)"**
   - 填写 **Note**：`wechat-bot deployment`
   - 选择 **Expiration**：`No expiration` 或选择有效期
   - 勾选权限：
     - ✅ `repo`（完全控制仓库）
     - ✅ `workflow`（GitHub Actions）

3. **生成并复制 Token**
   - 点击 **"Generate token"**
   - ⚠️ **立即复制 token**（只显示一次）
   - 格式：`ghp_xxxxxxxxxxxxxxxxxxxxxxxx`

#### 步骤2：使用 Token 推送代码

**方法 A：在命令行中输入**

```bash
cd /workspace/projects

# 推送时会提示输入用户名和密码
git push -u origin main

# 用户名：你的 GitHub 用户名（du118）
# 密码：刚才复制的 Personal Access Token
```

**方法 B：配置 Git 凭证存储**

```bash
# 配置 Git 使用 credential helper
git config --global credential.helper store

# 推送时输入一次认证信息
git push -u origin main

# 用户名：du118
# 密码：你的 Personal Access Token
```

**方法 C：使用 URL 中嵌入 Token（临时）**

```bash
# 使用 token 推送（一次性）
git push -u origin https://du118:你的Token@github.com/du118/wechat-bot.git main
```

---

### 方法2：使用 SSH 密钥（更安全）

#### 步骤1：生成 SSH 密钥

```bash
# 生成 SSH 密钥
ssh-keygen -t ed25519 -C "your_email@example.com"

# 或者使用 RSA
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

#### 步骤2：添加 SSH 密钥到 GitHub

1. **复制公钥**
   ```bash
   cat ~/.ssh/id_ed25519.pub
   # 或
   cat ~/.ssh/id_rsa.pub
   ```

2. **添加到 GitHub**
   - 访问：https://github.com/settings/keys
   - 点击 **"New SSH key"**
   - 粘贴公钥
   - 点击 **"Add SSH key"**

#### 步骤3：修改远程仓库 URL

```bash
cd /workspace/projects

# 修改远程仓库为 SSH
git remote set-url origin git@github.com:du118/wechat-bot.git

# 推送代码
git push -u origin main
```

---

### 方法3：使用 GitHub CLI（需要安装）

#### 步骤1：安装 GitHub CLI

```bash
# macOS
brew install gh

# Windows
# 从 https://cli.github.com/ 下载安装

# Linux
# 从 https://cli.github.com/ 下载安装
```

#### 步骤2：登录 GitHub

```bash
gh auth login

# 选择 GitHub.com
# 选择 HTTPS
# 选择 Yes（使用 web browser 登录）
```

#### 步骤3：推送代码

```bash
cd /workspace/projects
git push -u origin main
```

---

## 🚀 推荐操作步骤（方法1）

### 第一步：创建 Personal Access Token

1. 访问：https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 点击 "Generate token"
5. 复制 token（只显示一次）

### 第二步：推送代码

**在终端执行：**

```bash
cd /workspace/projects
git push -u origin main
```

**当提示输入：**
```
Username: du118
Password: 你的Personal Access Token（不是 GitHub 密码）
```

---

## 📊 推送成功后

推送成功后，你会看到：

```bash
Enumerating objects: 50, done.
Counting objects: 100% (50/50), done.
Delta compression using up to 8 threads
Compressing objects: 100% (30/30), done.
Writing objects: 100% (50/50), 50.00 KiB | 2.00 MiB/s, done.
Total 50 (delta 20), reused 40 (delta 15)
To https://github.com/du118/wechat-bot.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'origin' from 'main'.
```

然后访问：https://github.com/du118/wechat-bot 查看你的代码。

---

## 🔍 验证推送成功

1. **访问仓库**
   - 打开：https://github.com/du118/wechat-bot

2. **查看文件**
   - 应该能看到所有项目文件
   - 包括：`src/`, `config/`, `wsgi.py`, `Procfile` 等

---

## ❌ 常见问题

### 问题1：Authentication failed

**解决：**
- 确认 token 正确复制
- 确认 token 有 `repo` 权限
- 尝试重新生成 token

### 问题2：Permission denied

**解决：**
- 确认你有仓库的推送权限
- 确认 token 有 `repo` 权限

### 问题3：Token 无效

**解决：**
- Token 可能过期或被撤销
- 重新生成 token

---

## ✅ 推送成功后的下一步

推送成功后，继续：

1. **在微信云托管配置服务**
   - 仓库地址：`https://github.com/du118/wechat-bot`
   - 分支：`main`

2. **配置环境变量**
   - 添加 Coze API 密钥

3. **部署服务**
   - 点击"部署"

4. **配置微信公众号**
   - 使用云托管 URL

---

## 🎯 快速操作（最简单）

**只做 3 件事：**

1. **创建 Token**
   - 访问 https://github.com/settings/tokens
   - 生成新 token
   - 复制 token

2. **推送代码**
   ```bash
   cd /workspace/projects
   git push -u origin main
   ```
   - 用户名：`du118`
   - 密码：`你的 token`

3. **验证成功**
   - 访问 https://github.com/du118/wechat-bot

---

## 💡 提示

**Personal Access Token：**
- ⚠️ 类似于密码，要妥善保管
- ⚠️ 只在 GitHub 使用时生成
- ⚠️ 定期更新，提高安全性

**SSH 密钥：**
- ✅ 更安全，不需要每次输入密码
- ✅ 推荐长期使用
- ⚠️ 配置稍微复杂

**GitHub CLI：**
- ✅ 最方便
- ✅ 功能强大
- ⚠️ 需要安装

---

**创建 Token，然后执行推送命令！** 🚀
