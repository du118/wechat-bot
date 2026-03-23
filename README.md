# 🤖 星途纪元AI - 微信公众号机器人

基于 LangChain 和 Coze AI 的微信公众号智能机器人，支持多模态对话、联网搜索、语音交互等功能。

## ✨ 功能特性

- 🤖 **AI 智能对话** - 接入 Coze AI，支持复杂对话
- 🔍 **联网搜索** - 实时获取网络信息
- 🎤 **语音交互** - 支持语音输入和输出
- 📝 **多消息类型** - 支持文本、图片、语音消息
- 🚀 **高性能** - 优化响应速度和准确性
- 🌐 **微信公众号集成** - 无缝对接微信公众号

## 📋 技术栈

- **Python 3.12**
- **LangChain 1.0.3**
- **LangGraph 1.0.2**
- **Flask 3.1.3**
- **Coze AI SDK**
- **Gunicorn** (生产服务器)

## 🚀 部署方式

### 方式1：微信云托管（推荐）

#### 第一步：创建云托管服务

1. 访问：https://cloud.weixin.qq.com/
2. 点击"新建服务"
3. 服务名称：`wechat-bot`
4. 部署方式：GitHub 代码仓库
5. 仓库：`https://github.com/du118/wechat-bot.git`
6. 分支：`main`
7. 端口：`80`
8. Dockerfile：选择"有"，名称：`Dockerfile`

#### 第二步：配置环境变量

| 变量名 | 值 |
|--------|-----|
| `COZE_WORKSPACE_PATH` | `/workspace/projects` |
| `COZE_WORKLOAD_IDENTITY_API_KEY` | `你的Coze API密钥` |
| `COZE_INTEGRATION_MODEL_BASE_URL` | `你的Coze Base URL` |
| `UV_HTTP_TIMEOUT` | `300` |

**如何获取 Coze API 密钥：**
1. 登录 Coze 平台
2. 进入项目设置
3. 复制 API Key 和 Base URL

#### 第三步：部署服务

1. 点击"部署"
2. 等待 3-5 分钟
3. 获取公网 URL

#### 第四步：配置微信公众号

1. 登录：https://mp.weixin.qq.com/
2. 进入：开发 → 基本配置 → 服务器配置
3. 填写配置：

| 配置项 | 填写内容 |
|--------|----------|
| **URL** | `你的云托管URL/stream_run` |
| **Token** | `xingtuai2026` |
| **EncodingAESKey** | 点击"随机生成" |
| **消息加密** | 明文模式 |
| **数据格式** | XML |

4. 点击"确定"

---

### 方式2：Render 免费托管

#### 第一步：创建 Render 服务

1. 访问：https://render.com/
2. 注册并登录
3. 创建 Web Service
4. 连接 GitHub 仓库

#### 第二步：配置服务

- Name: `wechat-bot`
- Region: `Singapore`
- Branch: `main`
- Instance Type: `Free`

#### 第三步：部署

- 等待 3-5 分钟
- 获取 URL：`https://wechat-bot.onrender.com`

#### 第四步：配置微信公众号

- URL: `https://wechat-bot.onrender.com/stream_run`
- Token: `xingtuai2026`
- 其他配置同上

---

## 📁 项目结构

```
.
├── src/
│   ├── agents/
│   │   └── agent.py              # 智能体代码
│   ├── tools/
│   │   ├── web_search_tool.py    # 联网搜索工具
│   │   └── audio_tools.py        # 语音工具
│   ├── storage/
│   │   └── memory/
│   │       └── memory_saver.py   # 记忆存储
│   └── wechat_server.py          # 微信公众号服务器
├── config/
│   └── agent_llm_config.json     # LLM 配置
├── Dockerfile                    # Docker 镜像配置
├── Procfile                      # 启动配置
├── wsgi.py                       # WSGI 入口
├── requirements.txt              # Python 依赖
├── runtime.txt                   # Python 版本
└── README.md                     # 项目文档
```

## 🔧 本地开发

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置环境变量

```bash
export COZE_WORKSPACE_PATH=/workspace/projects
export COZE_WORKLOAD_IDENTITY_API_KEY=你的API密钥
export COZE_INTEGRATION_MODEL_BASE_URL=你的BaseURL
export UV_HTTP_TIMEOUT=300
```

### 启动服务

```bash
python src/wechat_server.py
```

或使用 Gunicorn：

```bash
gunicorn wsgi:app --bind 0.0.0.0:80 --workers 2 --timeout 120
```

## 🧪 测试

### 测试微信验证

```bash
python test_wechat_verification.py
```

### 测试消息收发

```bash
python test_wechat_message.py
```

## 📊 环境变量说明

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `COZE_WORKSPACE_PATH` | 工作目录路径 | ✅ |
| `COZE_WORKLOAD_IDENTITY_API_KEY` | Coze API 密钥 | ✅ |
| `COZE_INTEGRATION_MODEL_BASE_URL` | Coze API 地址 | ✅ |
| `UV_HTTP_TIMEOUT` | HTTP 超时时间 | ✅ |

## 🔑 Coze API 密钥获取

1. 登录 Coze 平台
2. 进入项目设置
3. 点击 "API Key"
4. 复制 API Key 和 Base URL

## ❌ 常见问题

### 问题1：部署失败 - 缺少 Dockerfile

**解决方案：**
- 确保仓库中包含 Dockerfile 文件
- 检查 Dockerfile 名称是否正确

### 问题2：微信配置失败

**解决方案：**
- 检查 URL 是否包含 `/stream_run`
- 检查 Token 是否为 `xingtuai2026`
- 查看云托管日志

### 问题3：AI 无法回复

**解决方案：**
- 检查 Coze API 密钥是否正确
- 检查环境变量是否配置
- 查看服务日志

## 📞 技术支持

- GitHub: https://github.com/du118/wechat-bot
- 微信云托管文档: https://cloud.weixin.qq.com/
- Coze 文档: https://www.coze.cn/docs

## 📄 许可证

MIT License

## 🙏 致谢

- [LangChain](https://github.com/langchain-ai/langchain)
- [Coze AI](https://www.coze.cn/)
- [微信云托管](https://cloud.weixin.qq.com/)

---

**星途纪元AI - 让对话更智能** 🚀
