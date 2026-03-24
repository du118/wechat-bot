#!/usr/bin/env python3
"""
测试 Coze API 密钥是否有效
"""

import os
import requests
import json

print("="*60)
print("Coze API 密钥测试")
print("="*60)

# 用户提供的 API 密钥
API_KEY = "pat_Z5Ido4vuuPiHRnty5puDpimODgMUUloXurjyFDIuYwaOOLQsjTmlK8h7LJMuclT1"

# 可能的 Base URL
BASE_URLS = [
    "https://api.coze.cn",
    "https://api.coze.com",
]

print(f"\nAPI Key: {API_KEY[:20]}...{API_KEY[-10:]}")
print("\n正在测试 API 密钥...\n")

# 测试每个 Base URL
for base_url in BASE_URLS:
    print(f"{'='*60}")
    print(f"测试 Base URL: {base_url}")
    print(f"{'='*60}\n")

    try:
        # 尝试调用 Coze API
        # 使用 /v1/chat/completions 端点测试
        test_url = f"{base_url}/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "doubao-seed-1-8-251228",
            "messages": [
                {"role": "user", "content": "你好"}
            ],
            "max_tokens": 10
        }

        print(f"发送请求到: {test_url}")
        print(f"请求头: Authorization: Bearer {API_KEY[:20]}...{API_KEY[-10:]}\n")

        response = requests.post(test_url, headers=headers, json=payload, timeout=30)

        print(f"响应状态码: {response.status_code}")
        print(f"响应头: {dict(response.headers)}\n")

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
            print("❌ API 密钥无效或过期")
            print(f"响应内容: {response.text}\n")
        elif response.status_code == 404:
            print("⚠️ API 端点不存在，尝试其他 Base URL\n")
        else:
            print(f"⚠️ 请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text}\n")

    except requests.exceptions.Timeout:
        print("❌ 请求超时\n")
    except requests.exceptions.ConnectionError as e:
        print(f"❌ 连接失败: {e}\n")
    except Exception as e:
        print(f"❌ 错误: {e}\n")

print(f"{'='*60}")
print("❌ 所有 Base URL 测试失败")
print(f"{'='*60}")
print("\n可能的原因：")
print("1. API 密钥无效或过期")
print("2. Base URL 不正确")
print("3. 网络连接问题")
print("4. 模型名称不正确")

exit(1)
