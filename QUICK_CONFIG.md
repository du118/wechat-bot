# 微信云托管快速配置卡片

## ✅ API 密钥验证成功

**API Key**: `pat_Z5Ido4vuuPiHRnty5puDpimODgMUUloXurjyFDIuYwaOOLQsjTmlK8h7LJMuclT1`
**Base URL**: `https://api.coze.cn`

---

## 📋 环境变量配置（直接复制）

请在微信云托管的服务设置中添加以下环境变量：

```
COZE_WORKSPACE_PATH=/app
COZE_WORKLOAD_IDENTITY_API_KEY=pat_Z5Ido4vuuPiHRnty5puDpimODgMUUloXurjyFDIuYwaOOLQsjTmlK8h7LJMuclT1
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn
UV_HTTP_TIMEOUT=300
```

---

## 🚀 5 步配置

### 1. 登录微信云托管
https://cloud.weixin.qq.com/

### 2. 进入服务 `flask-enou`

### 3. 点击"服务设置" → "环境变量"

### 4. 添加 4 个环境变量
- COZE_WORKSPACE_PATH
- COZE_WORKLOAD_IDENTITY_API_KEY
- COZE_INTEGRATION_MODEL_BASE_URL
- UV_HTTP_TIMEOUT

### 5. 保存 → 重新部署

---

## ✅ 配置完成标志

- [ ] 环境变量已添加
- [ ] 已保存配置
- [ ] 已重新部署
- [ ] 服务状态为"运行中"
- [ ] 运行日志中无错误

---

## 🎯 测试

配置完成后，测试微信公众号：

1. 关注公众号
2. 发送：`你好`
3. 等待回复（3-10秒）

---

**现在立即配置！** 🚀
