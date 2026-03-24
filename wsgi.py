#!/usr/bin/env python3
"""
WSGI 入口文件
用于 Render 部署
"""

import sys
import os

# 添加项目路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# 添加项目根目录和 src 目录到路径
if project_root not in sys.path:
    sys.path.insert(0, project_root)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 导入 Flask 应用
from src.wechat_server import app

if __name__ == '__main__':
    app.run()
