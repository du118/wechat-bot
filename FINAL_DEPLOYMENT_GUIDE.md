# 🚀 最终部署指南

## 📋 项目概述

**项目名称：** 星途纪元AI 微信公众号机器人

**功能：**
- 接收微信公众号消息
- 调用 Coze 智能体处理
- 自动回复用户消息
- 支持文本、图片、语音消息

**部署平台：** Render（免费）

---

## ✅ 前置准备

### 必需账号
- ✅ GitHub 账号
- ✅ Render 账号（https://render.com/）
- ✅ 微信公众号（个人订阅号即可）

### 项目文件清单
```
/workspace/projects/
├── src/
│   ├── agents/
│   │   └── agent.py              # 智能体代码
│   ├── tools/
│   │   ├── web_search_tool.py
│   │   └── audio_tools.py
│   └── wechat_server.py          # Flask 服务器
├── config/
│   └── agent_llm_config.json     # LLM 配置
├── wsgi.py                       # WSGI 入口 ✅
├── Procfile                      # 启动命令 ✅
├── requirements.txt              # Python 依赖 ✅
├── runtime.txt                   # Python 版本 ✅
├── .gitignore                    # Git 忽略 ✅
└── README.md
```

---

## 🚀 部署步骤（10分钟搞定）

### 第一步：创建 GitHub 仓库（2分钟）

1. 访问 https://github.com/
2. 点击 "New repository"
3. 填写：
   - **Repository name**: `wechat-bot`
   - 选择 **Public**
4. 点击 "Create repository"
5. 复制仓库 URL：
   ```
   https://github.com/你的用户名/wechat-bot.git
   ```

---

### 第二步：上传代码到 GitHub（2分钟）

在项目目录执行：

```bash
# 初始化 Git
git init

# 添加所有文件
git add .

# 提交
git commit -m "WeChat bot with Coze integration"

# 添加远程仓库（替换成你的用户名）
git remote add origin https://github.com/你的用户名/wechat-bot.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

---

### 第三步：在 Render 创建服务（3分钟）

1. 打开 https://render.com/
2. 点击 "Sign Up" 注册
3. 使用 GitHub 账号登录
4. 点击 "New +"
5. 选择 "Web Service"
6. 点击 "Connect GitHub" 授权
7. 选择 `wechat-bot` 仓库
8. 填写配置：

| 配置项 | 填写内容 |
|--------|----------|
| **Name** | `wechat-bot` |
| **Region** | `Singapore`（亚洲访问快） |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | 留空 |
| **Start Command** | 留空 |
| **Instance Type** | `Free` |

9. 点击 "Create Web Service"

---

### 第四步：等待部署（3分钟）

Render 会自动：
1. 克隆代码
2. 安装依赖
3. 启动服务

**查看部署进度：**
- 点击服务名称
- 查看 "Logs" 标签
- 等待 "Deploy succeeded"

**部署时间：** 3-5 分钟

---

### 第五步：获取 Render URL

部署成功后：

1. 在服务详情页顶部找到 **URL**
2. 格式类似：
   ```
   https://wechat-bot.onrender.com
   ```
3. **复制这个 URL**

---

### 第六步：配置微信公众号（2分钟）

1. 登录微信公众号：https://mp.weixin.qq.com/
2. 进入 "开发" → "基本配置" → "服务器配置"
3. 填写配置：

| 配置项 | 填写内容 |
|--------|----------|
| **URL** | `https://wechat-bot.onrender.com/stream_run` |
| **Token** | `xingtuai2026` |
| **EncodingAESKey** | 点击"随机生成" |
| **消息加密** | 选择 **明文模式** |
| **数据格式** | XML |

4. 点击 "确定"

---

### 第七步：验证配置成功

如果配置成功，会显示：
```
服务器配置已生效
```

如果失败，检查：
- Render 服务是否正在运行
- URL 是否正确（包括 `/stream_run`）
- Token 是否为 `xingtuai2026`

---

### 第八步：测试功能（2分钟）

1. **用另一个微信关注你的公众号**
2. **发送消息**："你好"
3. **观察是否收到回复**

---

## ✅ 部署检查清单

- [x] GitHub 仓库已创建
- [x] 代码已上传到 GitHub
- [x] Render 服务已创建
- [x] 服务已部署成功
- [x] Render URL 已获取
- [x] 微信公众号已配置
- [x] 配置验证成功
- [x] 消息收发测试通过

---

## 📊 项目结构

```
用户（微信）
   ↓ 发送消息
   ↓
微信公众号（腾讯）
   ↓ POST 请求
   ↓
Render 免费服务器
   ↓ URL: https://wechat-bot.onrender.com/stream_run
   ↓
Flask 服务器 (wechat_server.py)
   ↓ 接收消息
   ↓
Coze 智能体 (云端)
   ↓ 处理消息
   ↓
Flask 服务器
   ↓ 返回 XML 回复
   ↓
微信公众号
   ↓ 发送给用户
   ↓
用户收到回复
```

---

## 🔍 常见问题

### 问题1：部署失败

**检查：**
1. 查看部署日志
2. 检查 `requirements.txt` 是否有语法错误
3. 检查 `Procfile` 格式是否正确

### 问题2：404 Not Found

**解决：**
1. 确认 `wsgi.py` 文件存在
2. 确认 `Procfile` 中是 `wsgi:app`
3. 清除构建缓存重新部署

### 问题3：微信配置失败（HTTP返回非200）

**解决：**
1. 确认 Render 服务正在运行
2. 确认 URL 正确（包括 `/stream_run`）
3. 确认 Token 为 `xingtuai2026`
4. 查看 Render 日志

### 问题4：服务休眠

**说明：** Render 免费版会在 15 分钟无请求后自动休眠

**解决：**
1. 第一次请求会唤醒服务（30-60 秒）
2. 定期发送请求保持活跃
3. 或升级到付费版（$7/月）

---

## 💰 成本说明

**Render 免费额度：**
- 实例数：1 个
- CPU：512MB
- 内存：512MB
- 运行时间：750 小时/月
- 带宽：100GB/月

**对于个人公众号：**
- ✅ 完全够用
- ✅ 基本免费
- ✅ 24小时在线

---

## 🎯 功能特性

✅ **完全免费** - 个人项目永久免费
✅ **无需云托管** - 不是微信云托管
✅ **无需内网穿透** - 不需要你的电脑在线
✅ **自动运行** - 24小时在线
✅ **多消息类型** - 支持文本、图片、语音
✅ **AI 智能回复** - 接入 Coze 智能体
✅ **简单部署** - 连接 GitHub 即可

---

## 📞 技术支持

### 遇到问题？

1. **查看日志**
   - Render: 服务详情 → Logs
   - 微信: 查看配置反馈

2. **常见错误**
   - 404: 检查 wsgi.py 和 Procfile
   - 401: 检查 Token 配置
   - 500: 查看服务器日志

3. **获取帮助**
   - 查看项目文档
   - 查看 GitHub Issues

---

## 🎉 完成！

现在你的微信公众号已经成功连接到 Coze 智能体！

**特点：**
- ✅ 完全免费
- ✅ 无需云托管
- ✅ 无需内网穿透
- ✅ 24小时在线
- ✅ 自动回复

---

**祝你部署成功！** 🚀

**有问题随时联系！** 💬
