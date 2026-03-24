#!/usr/bin/env python3
"""
微信云托管环境检测和测试脚本
"""

import os
import sys
import requests
import json
from datetime import datetime

print("="*60)
print("微信云托管环境检测")
print("="*60)

# 1. 检查环境变量
print("\n【1. 检查环境变量】")

required_vars = {
    'COZE_WORKSPACE_PATH': '/workspace/projects',
    'COZE_WORKLOAD_IDENTITY_API_KEY': '必须配置',
    'COZE_INTEGRATION_MODEL_BASE_URL': '必须配置',
    'PORT': '80',
}

all_good = True

for var, expected in required_vars.items():
    value = os.environ.get(var, '未设置')
    status = "✅" if value and value != '未设置' else "❌"
    print(f"{status} {var}: {value}")

    if expected == '必须配置' and not value:
        all_good = False

if not all_good:
    print("\n⚠️ 警告：部分必需的环境变量未配置！")
    print("请在微信云托管中配置以下环境变量：")
    print("- COZE_WORKLOAD_IDENTITY_API_KEY")
    print("- COZE_INTEGRATION_MODEL_BASE_URL")
else:
    print("\n✅ 所有环境变量配置正确！")

# 2. 检查配置文件
print("\n【2. 检查配置文件】")

try:
    workspace_path = os.getenv('COZE_WORKSPACE_PATH', '/workspace/projects')
    config_file = os.path.join(workspace_path, 'config/agent_llm_config.json')

    with open(config_file, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

    print(f"✅ 配置文件读取成功：{config_file}")
    print(f"   模型: {cfg['config']['model']}")
    print(f"   温度: {cfg['config']['temperature']}")
    print(f"   超时: {cfg['config']['timeout']}秒")

except Exception as e:
    print(f"❌ 配置文件读取失败：{e}")
    all_good = False

# 3. 测试 Agent 构建
print("\n【3. 测试 Agent 构建】")

try:
    sys.path.insert(0, workspace_path)
    from agents.agent import build_agent

    agent = build_agent()
    print(f"✅ Agent 构建成功！")

except Exception as e:
    print(f"❌ Agent 构建失败：{e}")
    import traceback
    traceback.print_exc()
    all_good = False

# 4. 测试微信公众号验证接口
print("\n【4. 测试微信公众号验证接口】")

try:
    # 获取服务 URL
    port = os.getenv('PORT', '80')
    local_url = f"http://localhost:{port}/stream_run"

    # 构造验证请求
    import hashlib
    token = 'xingtuai2026'
    timestamp = str(int(datetime.now().timestamp()))
    nonce = 'test123'

    # 生成签名
    tmp_list = [token, timestamp, nonce]
    tmp_list.sort()
    tmp_str = ''.join(tmp_list)
    signature = hashlib.sha1(tmp_str.encode()).hexdigest()

    test_url = f"{local_url}?signature={signature}&timestamp={timestamp}&nonce={nonce}&echostr=test123"

    print(f"测试URL: {test_url}")

    # 发送请求
    response = requests.get(test_url, timeout=5)

    print(f"响应状态码: {response.status_code}")
    print(f"响应内容: {response.text}")

    if response.status_code == 200 and response.text == 'test123':
        print(f"✅ 微信验证接口测试成功！")
    else:
        print(f"❌ 微信验证接口测试失败！")
        all_good = False

except Exception as e:
    print(f"❌ 微信验证接口测试失败：{e}")
    import traceback
    traceback.print_exc()
    all_good = False

# 5. 总结
print("\n" + "="*60)
print("检测结果总结")
print("="*60)

if all_good:
    print("✅ 所有检测项通过！环境配置正确。")
    print("\n下一步：")
    print("1. 确保微信公众号配置的 Token 为: xingtuai2026")
    print("2. 确保微信公众号配置的 URL 包含 /stream_run 路径")
    print("3. 在微信公众号中发送测试消息")
    sys.exit(0)
else:
    print("❌ 检测失败！请修复上述问题后再试。")
    print("\n常见问题：")
    print("1. 环境变量未配置 - 请在微信云托管中配置 COZE_WORKLOAD_IDENTITY_API_KEY 和 COZE_INTEGRATION_MODEL_BASE_URL")
    print("2. Agent 构建失败 - 检查配置文件和代码")
    print("3. 微信验证接口失败 - 检查 URL 和 Token 配置")
    sys.exit(1)
