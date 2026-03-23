# 微信云托管部署修复方案

## 🐛 当前错误

**错误信息：**
```
× No solution found when resolving dependencies:
╰─▶ Because alembic was not found in the package registry and you
    require alembic==1.18.4, we can conclude that your requirements are
    unsatisfiable.

hint: An index URL (https://pypi.tuna.tsinghua.edu.cn/simple/) returned
    a 403 Forbidden error.
```

**问题原因：**
- 清华镜像源返回 403 Forbidden 错误
- 导致 uv 无法解析依赖

---

## ✅ 修复方案

### 方案1：使用阿里云镜像（当前方案）

**已修改的文件：**

#### 1. pyproject.toml
```toml
[tool.uv]
# 使用阿里云镜像作为默认源
# 阿里云镜像更稳定，兼容性更好
[[tool.uv.index]]
url = "https://mirrors.aliyun.com/pypi/simple/"
default = true

# 增加 HTTP 超时时间，防止大文件下载超时
http_timeout = 300
```

#### 2. .env
```bash
UV_HTTP_TIMEOUT=300
UV_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
PYTHONUNBUFFERED=1
```

#### 3. requirements.txt
```txt
# 已降级 zstandard
zstandard==0.23.0  # 原来是 0.25.0
```

---

### 方案2：使用官方 PyPI 源（备选方案）

如果阿里云镜像也有问题，可以使用官方源：

**修改 pyproject.toml：**
```toml
[tool.uv]
# 使用官方 PyPI 源
[[tool.uv.index]]
url = "https://pypi.org/simple/"
default = true

# 增加 HTTP 超时时间
http_timeout = 300
```

**修改 .env：**
```bash
UV_HTTP_TIMEOUT=300
UV_INDEX_URL=https://pypi.org/simple/
PYTHONUNBUFFERED=1
```

---

### 方案3：使用豆瓣镜像（备选方案）

如果官方源也慢，可以使用豆瓣镜像：

**修改 pyproject.toml：**
```toml
[tool.uv]
# 使用豆瓣镜像
[[tool.uv.index]]
url = "https://pypi.doubanio.com/simple/"
default = true

# 增加 HTTP 超时时间
http_timeout = 300
```

**修改 .env：**
```bash
UV_HTTP_TIMEOUT=300
UV_INDEX_URL=https://pypi.doubanio.com/simple/
PYTHONUNBUFFERED=1
```

---

## 🚀 重新部署步骤

### 第一步：确认配置

检查以下配置是否正确：

1. **pyproject.toml**
   - 镜像源：`https://mirrors.aliyun.com/pypi/simple/`
   - 超时时间：`300`

2. **.env**
   - `UV_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/`
   - `UV_HTTP_TIMEOUT=300`

3. **requirements.txt**
   - `zstandard==0.23.0`

### 第二步：重新部署

1. 进入微信云托管控制台
2. 选择你的服务
3. 点击"重新部署"
4. 等待部署完成

### 第三步：观察部署日志

**成功的情况：**
```
info: [build] [runtime] Resolved 136 packages in xxxs
info: [build] [runtime] Pipeline run success
info: [launch] Deployment success
```

**如果还是失败：**
查看具体的错误信息，可能是：
- 镜像源问题 → 尝试方案2或方案3
- 依赖冲突 → 检查版本号
- 网络问题 → 增加超时时间

---

## 🔍 本地测试

在重新部署前，可以在本地测试：

```bash
# 测试依赖解析
uv lock

# 如果成功，会显示：
# Resolved 136 packages in xxxms

# 测试依赖安装
uv sync

# 测试启动服务
bash start.sh
```

---

## 📊 镜像源对比

| 镜像源 | URL | 速度 | 稳定性 | 推荐度 |
|--------|-----|------|--------|--------|
| **阿里云** | https://mirrors.aliyun.com/pypi/simple/ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 推荐 |
| **清华** | https://pypi.tuna.tsinghua.edu.cn/simple/ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ❌ 403错误 |
| **豆瓣** | https://pypi.doubanio.com/simple/ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 备选 |
| **官方PyPI** | https://pypi.org/simple/ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 备选 |

---

## 🆘 常见问题

### 问题1：镜像源 403 错误

**解决方案：**
- 切换到其他镜像源（阿里云 / 豆瓣 / 官方）
- 或者等待镜像源恢复

### 问题2：依赖解析失败

**解决方案：**
- 检查 `requirements.txt` 是否有语法错误
- 确认依赖版本号是否正确
- 尝试放宽版本限制（如 `>=` 替代 `==`）

### 问题3：下载超时

**解决方案：**
- 增加 `UV_HTTP_TIMEOUT`（已设置为 300 秒）
- 使用更快的镜像源
- 减少不必要的依赖

---

## ✅ 验证清单

部署前请确认：

- [x] 修改 `pyproject.toml` 使用阿里云镜像
- [x] 修改 `.env` 设置正确的镜像源
- [x] 降级 `zstandard` 到 0.23.0
- [x] 本地测试 `uv lock` 成功
- [ ] 提交代码到微信云托管
- [ ] 重新部署
- [ ] 验证部署成功

---

## 📞 如果还有问题

如果部署仍然失败，请提供：

1. 完整的错误日志
2. 当前使用的镜像源
3. uv 版本号
4. Python 版本号

这些信息可以帮助快速定位问题。
