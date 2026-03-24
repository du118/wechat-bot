# 微信云托管环境变量配置指南

## ✅ API 密钥验证结果

**状态**: ✅ 有效
**Base URL**: `https://api.coze.cn`
**API Key**: `pat_Z5Ido4vuuPiHRnty5puDpimODgMUUloXurjyFDIuYwaOOLQsjTmlK8h7LJMuclT1`

---

## 📋 需要配置的环境变量

请在微信云托管中配置以下环境变量：

| 环境变量 | 值 | 说明 |
|----------|-----|------|
| `COZE_WORKSPACE_PATH` | `/app` | 工作目录（Docker 容器路径） |
| `COZE_WORKLOAD_IDENTITY_API_KEY` | `pat_Z5Ido4vuuPiHRnty5puDpimODgMUUloXurjyFDIuYwaOOLQsjTmlK8h7LJMuclT1` | Coze API 密钥 |
| `COZE_INTEGRATION_MODEL_BASE_URL` | `https://api.coze.cn` | Coze API 地址 |
| `UV_HTTP_TIMEOUT` | `300` | HTTP 超时时间（秒） |

---

## 🚀 配置步骤

### 第一步：登录微信云托管

访问：https://cloud.weixin.qq.com/

### 第二步：进入服务设置

1. 找到你的服务：`flask-enou`
2. 点击服务名称进入服务详情页
3. 点击顶部的 **"服务设置"** 标签

### 第三步：配置环境变量

1. 在服务设置页面，找到 **"环境变量"** 或 **"配置"** 区域
2. 点击 **"添加环境变量"** 或 **"新建"**
3. 逐个添加以下环境变量：

```
COZE_WORKSPACE_PATH=/app
COZE_WORKLOAD_IDENTITY_API_KEY=pat_Z5Ido4vuuPiHRnty5puDpimODgMUUloXurjyFDIuYwaOOLQsjTmlK8h7LJMuclT1
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn
UV_HTTP_TIMEOUT=300
```

**重要提醒**：
- ⚠️ 不要有空格
- ⚠️ 值必须完全一致
- ⚠️ `/app` 不是 `/workspace/projects`

### 第四步：保存配置

1. 确认所有环境变量都已添加
2. 点击 **"保存"** 或 **"应用"**
3. 等待保存完成

### 第五步：重新部署服务

1. 返回服务详情页
2. 点击 **"部署"** → **"重新部署"**
3. 或点击 **"新建版本"**
4. 等待 3-5 分钟

---

## 🧪 验证配置

### 方法 1：查看运行日志

1. 进入 **"运行日志"** 页面
2. 查看启动日志
3. 应该看到：

```
星途纪元AI - 微信公众号服务器启动中...
Token配置：xingtuai2026
监听地址：0.0.0.0:80
```

### 方法 2：运行测试脚本

```bash
python test_wechat_connection.py
python test_wechat_message.py
```

### 方法 3：测试微信公众号

1. 关注你的微信公众号
2. 发送消息：`你好`
3. 等待 AI 回复（应该 3-10 秒内收到）

---

## ✅ 配置完成后的检查清单

- [ ] 环境变量 `COZE_WORKSPACE_PATH` 配置为 `/app`
- [ ] 环境变量 `COZE_WORKLOAD_IDENTITY_API_KEY` 配置为你的密钥
- [ ] 环境变量 `COZE_INTEGRATION_MODEL_BASE_URL` 配置为 `https://api.coze.cn`
- [ ] 环境变量 `UV_HTTP_TIMEOUT` 配置为 `300`
- [ ] 已保存环境变量配置
- [ ] 已重新部署服务
- [ ] 服务状态为"运行中"
- [ ] 运行日志中无错误

---

## ❌ 常见问题

### Q1: 配置后还是无法工作？

**解决方案**：
1. 确认环境变量名称和值完全正确
2. 必须重新部署服务才能生效
3. 查看运行日志是否有错误

### Q2: API 密钥不工作？

**解决方案**：
1. 确认密钥格式：`pat_xxxxx`
2. 确认 Base URL 为 `https://api.coze.cn`
3. 在 Coze 平台重新生成密钥

### Q3: 服务启动失败？

**解决方案**：
1. 检查运行日志
2. 确认 `COZE_WORKSPACE_PATH` 为 `/app`
3. 重新部署服务

---

## 🎯 预期结果

配置成功并重新部署后：

1. ✅ 服务正常启动
2. ✅ 微信公众号验证成功
3. ✅ 可以接收和处理微信消息
4. ✅ AI 正常回复

---

## 📞 需要帮助？

如果配置后仍有问题，请提供：

1. 微信云托管的运行日志
2. 环境变量配置截图（隐藏密钥）
3. 服务状态截图

---

**现在请立即按照上述步骤配置环境变量！** 🚀
