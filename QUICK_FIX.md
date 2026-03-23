# 修复 Render 404 错误

## 🐛 问题

访问 `https://wechat-bot.onrender.com/stream_run` 返回 **Not Found (404)**

## ✅ 已修复

### 修改的文件

#### 1. 新建 `wsgi.py`
```python
#!/usr/bin/env python3
"""
WSGI 入口文件
用于 Render 部署
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入 Flask 应用
from src.wechat_server import app

if __name__ == '__main__':
    app.run()
```

#### 2. 修改 `Procfile`
```
web: gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

**变化：** `src.wechat_server:app` → `wsgi:app`

---

## 🚀 重新部署步骤

### 第一步：提交修改到 GitHub

```bash
# 添加所有修改
git add .

# 提交
git commit -m "Fix 404 error: add wsgi.py and update Procfile"

# 推送到 GitHub
git push origin main
```

### 第二步：触发 Render 重新部署

1. 打开 https://dashboard.render.com/
2. 找到 `wechat-bot` 服务
3. 点击进入服务详情
4. 点击 "Manual Deploy" → "Clear build cache & deploy"
5. 等待部署完成（3-5分钟）

### 第三步：验证部署成功

1. 部署完成后，访问你的 Render URL：
   ```
   https://wechat-bot.onrender.com/stream_run
   ```

2. **如果看到以下内容，说明成功：**
   - 空白页面
   - 或者 "Method Not Allowed"（正常，因为你用浏览器访问 GET 请求）

3. **如果还是看到 "Not Found"：**
   - 查看 Render 日志
   - 检查是否有错误

### 第四步：配置微信公众号

#### 填写配置：

| 配置项 | 填写内容 |
|--------|----------|
| **URL** | `https://wechat-bot.onrender.com/stream_run` |
| **Token** | `xingtuai2026` |
| **EncodingAESKey** | 点击"随机生成" |
| **消息加密** | 明文模式 ✅ |
| **数据格式** | XML ✅ |

#### 点击"确定"

如果配置成功，你会看到：
```
服务器配置已生效
```

---

## 🔍 查看日志

如果部署失败，查看日志：

1. 打开 https://dashboard.render.com/
2. 找到 `wechat-bot` 服务
3. 点击 "Logs" 标签
4. 查看最新日志

**可能的错误：**
- `ModuleNotFoundError` → 检查 requirements.txt
- `ImportError` → 检查文件路径
- `404 Not Found` → 检查路由定义

---

## 📊 验证路由

### 本地测试

```bash
# 测试应用是否可以导入
python -c "from src.wechat_server import app; print('Success')"

# 测试 wsgi 是否可以导入
python -c "import wsgi; print('Success')"

# 测试路由
python -c "from src.wechat_server import app; print([rule.rule for rule in app.url_map.iter_rules()])"
```

**应该输出：**
```
['/static/<path:filename>', '/stream_run']
```

### 在线测试

访问：
```
https://wechat-bot.onrender.com/stream_run
```

**预期结果：**
- ✅ 空白页面
- ✅ 或 "Method Not Allowed"
- ❌ 不是 "Not Found"

---

## ✅ 完成检查清单

- [x] 创建 `wsgi.py` 文件
- [x] 修改 `Procfile`
- [ ] 提交修改到 GitHub
- [ ] 触发 Render 重新部署
- [ ] 验证 URL 可以访问
- [ ] 配置微信公众号
- [ ] 测试消息收发

---

## 🎉 预期结果

配置成功后：

1. ✅ 访问 `https://wechat-bot.onrender.com/stream_run` 不再出现 404
2. ✅ 微信公众号配置成功
3. ✅ 用户发送消息后，AI 自动回复

---

## 🆘 问题排查

### 问题1：部署失败

**检查：**
1. Render 日志中的错误信息
2. 是否所有依赖都已安装
3. 是否有语法错误

### 问题2：URL 还是 404

**检查：**
1. 服务是否正在运行（查看 Render 状态）
2. 路由是否正确定义
3. 是否清除了构建缓存

### 问题3：微信配置失败

**检查：**
1. URL 是否正确（包括 `/stream_run`）
2. Token 是否为 `xingtuai2026`
3. Render 服务是否正在运行
4. Render 日志中是否收到请求

---

**按照步骤操作，问题应该就解决了！** 🚀
