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
