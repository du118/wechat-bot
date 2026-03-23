#!/bin/bash
# 微信云托管启动脚本

# 设置 UV 相关环境变量
export UV_HTTP_TIMEOUT=300
export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

# 设置 Python 环境变量
export PYTHONUNBUFFERED=1

# 安装依赖（如果需要）
# uv sync

# 启动 Flask 服务器
# 根据云托管环境变量 PORT 设置端口
export PORT=${PORT:-80}

echo "============================================================"
echo "星途纪元AI - 微信公众号服务器启动中..."
echo "============================================================"
echo "PORT: $PORT"
echo "UV_HTTP_TIMEOUT: $UV_HTTP_TIMEOUT"
echo "============================================================"

# 使用 gunicorn 启动（如果已安装）
if command -v gunicorn &> /dev/null; then
    echo "使用 gunicorn 启动服务器..."
    gunicorn src.wechat_server:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
else
    echo "使用 Flask 开发服务器启动..."
    python src/wechat_server.py
fi
