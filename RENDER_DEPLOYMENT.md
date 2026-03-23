# 使用 Render 免费托管微信公众号服务器

## 🎯 方案优势

✅ **完全免费** - 个人项目永久免费
✅ **无需云托管** - 不是微信云托管
✅ **无需内网穿透** - 不需要你的电脑在线
✅ **简单部署** - 连接 GitHub 即可
✅ **公网 URL** - 自动提供公网访问地址
✅ **自动运行** - 24小时在线

---

## 📋 准备工作

### 第一步：确认文件已准备

确保你的项目目录包含以下文件：

```
/workspace/projects/
├── src/
│   ├── agents/
│   │   └── agent.py              # 智能体代码
│   ├── tools/
│   └── wechat_server.py          # Flask 服务器（已修改）
├── config/
│   └── agent_llm_config.json     # LLM 配置
├── requirements.txt              # Python 依赖
├── pyproject.toml                # 项目配置
├── Procfile                      # 启动命令（已修改）
├── runtime.txt                   # Python 版本
├── start.sh                      # 启动脚本
├── .gitignore                    # Git 忽略文件
└── README.md
```

### 第二步：注册 Render 账号

1. 访问 Render 官网：https://render.com/
2. 点击 "Sign Up" 注册账号
3. 使用 GitHub 账号登录（推荐）
4. 完成账号设置

---

## 🚀 部署步骤

### 步骤1：创建 GitHub 仓库

如果你还没有 GitHub 仓库，需要创建一个：

1. 访问 GitHub：https://github.com/
2. 点击 "New repository"
3. 填写仓库名称：`wechat-bot`（或你喜欢的名称）
4. 设置为 Public（公开）
5. 点击 "Create repository"

### 步骤2：上传代码到 GitHub

在你的项目目录执行：

```bash
# 初始化 Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: WeChat bot with Coze integration"

# 添加远程仓库
git remote add origin https://github.com/你的用户名/你的仓库名.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 步骤3：在 Render 上创建服务

1. 登录 Render：https://dashboard.render.com/
2. 点击 "New +"
3. 选择 "Web Service"
4. 连接你的 GitHub 账号
5. 选择你刚才创建的仓库
6. 填写以下配置：

**Name**: `wechat-bot`（或你喜欢的名称）

**Region**: `Singapore`（新加坡，亚洲地区访问快）

**Branch**: `main`

**Runtime**: `Python 3`

**Build Command**: 留空（会自动检测）

**Start Command**: 留空（会使用 Procfile）

**Instance Type**: `Free`

7. 点击 "Create Web Service"

### 步骤4：等待部署

Render 会自动：
1. 克隆你的代码
2. 安装依赖
3. 启动服务

这个过程通常需要 3-5 分钟。

---

## 🔧 获取公网 URL

部署成功后：

1. 在 Render 控制台，找到你的服务
2. 点击服务名称进入详情页
3. 在顶部可以看到 **URL**，例如：
   ```
   https://wechat-bot.onrender.com
   ```
4. 复制这个 URL

---

## ⚙️ 配置微信公众号

### 第一步：进入微信公众号后台

1. 登录微信公众号：https://mp.weixin.qq.com/
2. 进入 "开发" → "基本配置" → "服务器配置"

### 第二步：填写配置信息

| 配置项 | 填写内容 |
|--------|----------|
| **URL** | `https://wechat-bot.onrender.com/stream_run`（将 wechat-bot 替换为你的服务名） |
| **Token** | `xingtuai2026` |
| **EncodingAESKey** | 点击"随机生成" |
| **消息加密** | 选择 **明文模式** |
| **数据格式** | XML |

### 第三步：提交配置

点击 "确定" 按钮

### 第四步：验证成功

如果配置成功，会显示：
```
服务器配置已生效
```

---

## 🧪 测试功能

### 测试1：验证配置成功

1. 在浏览器中访问你的 Render URL：
   ```
   https://wechat-bot.onrender.com/stream_run
   ```

2. 如果看到类似 "Method Not Allowed" 或空白页面，说明服务正常运行。

### 测试2：发送测试消息

1. 用另一个微信关注你的公众号
2. 发送消息："你好"
3. 观察是否收到 AI 回复

### 测试3：查看日志

在 Render 控制台，点击你的服务：
- 点击 "Logs" 标签
- 查看实时的请求日志
- 确认消息是否正常接收和处理

---

## 🔍 常见问题

### 问题1：部署失败

**错误信息：** `Build failed`

**解决方案：**
1. 检查 `requirements.txt` 是否有语法错误
2. 检查 `Procfile` 格式是否正确
3. 查看部署日志，找到具体错误

### 问题2：服务启动失败

**错误信息：** `Service failed to start`

**解决方案：**
1. 检查 `Procfile` 中的启动命令
2. 确认 `src/wechat_server.py` 文件路径正确
3. 查看服务日志

### 问题3：微信公众号配置失败

**错误信息：** `HTTP返回非200` 或 `Token验证失败`

**解决方案：**
1. 确认 Render 服务正在运行
2. 确认 URL 正确（不要忘记 `/stream_run` 路径）
3. 确认 Token 填写为 `xingtuai2026`
4. 查看 Render 日志，确认是否收到微信的验证请求

### 问题4：服务休眠

**说明：** Render 免费版会在 15 分钟无请求后自动休眠

**解决方案：**
1. 第一次请求会唤醒服务（需要 30-60 秒）
2. 定期发送请求保持服务活跃
3. 或者升级到付费版（约 $7/月）

---

## 📊 Render 免费额度

Render 免费版提供：

| 资源 | 免费额度 |
|------|----------|
| **实例数** | 1 个 |
| **CPU** | 512MB |
| **内存** | 512MB |
| **运行时间** | 750 小时/月 |
| **带宽** | 100GB/月 |

**对于个人微信公众号：**
- ✅ 完全够用
- ✅ 基本免费
- ✅ 24小时在线

---

## 🎉 完成

现在你的微信公众号已经成功连接到 Coze 智能体！

**特点：**
- ✅ 完全免费
- ✅ 无需云托管
- ✅ 无需内网穿透
- ✅ 24小时在线
- ✅ 自动回复

---

## 📞 需要帮助？

如果遇到问题：

1. 查看 Render 服务日志
2. 检查微信公众号配置
3. 查看 Render 文档：https://render.com/docs

---

## 🔄 后续优化

如果需要更强的性能：

1. **升级 Render 服务**
   - 升级到 Standard ($7/月)
   - 更快的响应速度
   - 不会自动休眠

2. **使用多个服务**
   - 负载均衡
   - 更高的并发

3. **添加缓存**
   - Redis 缓存
   - 更快的响应

---

**祝你部署成功！** 🚀
