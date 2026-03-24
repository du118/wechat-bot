#!/usr/bin/env python3
"""
测试 Coze API 密钥 - 尝试多个端点
"""

import os
import requests
import json

print("="*60)
print("Coze API 密钥测试")
print("="*60)

# 用户提供的 API 密钥
API_KEY = "pat_Z5Ido4vuuPiHRnty5puDpimODgMUUloXurjyFDIuYwaOOLQsjTmlK8h7LJMuclT1"

# 可能的 Base URL 和端点组合
ENDPOINTS = [
    ("https://api.coze.cn", "/v1/chat"),
    ("https://api.coze.cn", "/v1/chat/completions"),
    ("https://api.coze.cn", "/v3/chat"),
    ("https://api.coze.cn", "/v3/chat/completions"),
    ("https://api.coze.cn", "/open_api/v2/chat"),
    ("https://api.coze.cn", "/open_api/v3/chat"),
    ("https://api.coze.com", "/v1/chat"),
    ("https://api.coze.com", "/v1/chat/completions"),
    ("https://api.coze.com", "/v3/chat"),
    ("https://api.coze.com", "/v3/chat/completions"),
]

print(f"\nAPI Key: {API_KEY[:20]}...{API_KEY[-10:]}")
print("\n正在测试多个端点...\n")

for base_url, endpoint in ENDPOINTS:
    print(f"{'='*60}")
    print(f"测试: {base_url}{endpoint}")
    print(f"{'='*60}\n")

    try:
        test_url = f"{base_url}{endpoint}"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "bot_id": "7383325185888784445",  # Coze 的默认 bot_id
            "user": "test_user",
            "query": "你好",
            "stream": False
        }

        print(f"发送请求...")

        response = requests.post(test_url, headers=headers, json=payload, timeout=30)

        print(f"响应状态码: {response.status_code}")

        if response.status_code == 200:
            print("✅ API 密钥验证成功！")
            print(f"\n响应内容:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

            print(f"{'='*60}")
            print("✅ 推荐配置")
            print(f"{'='*60}")
            print(f"COZE_WORKLOAD_IDENTITY_API_KEY={API_KEY}")
            print(f"COZE_INTEGRATION_MODEL_BASE_URL={base_url}")
            print(f"COZE_WORKSPACE_PATH=/app")
            print(f"UV_HTTP_TIMEOUT=300\n")

            exit(0)
        elif response.status_code == 401:
            print("❌ API 密钥无效或过期\n")
        elif response.status_code == 404:
            print("⚠️ 端点不存在\n")
        else:
            print(f"状态码: {response.status_code}")
            print(f"响应: {response.text[:200]}\n")

    except requests.exceptions.Timeout:
        print("❌ 请求超时\n")
    except requests.exceptions.ConnectionError as e:
        print(f"❌ 连接失败: {e}\n")
    except Exception as e:
        print(f"❌ 错误: {e}\n")

print(f"{'='*60}")
print("❌ 所有端点测试失败")
print(f"{'='*60}")
print("\n建议：")
print("1. 确认 API 密钥是否有效")
print("2. 检查 Coze 平台的 API 文档")
print("3. 联系 Coze 技术支持")

exit(1)
