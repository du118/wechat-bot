#!/usr/bin/env python3
"""
测试微信云托管和微信公众号的连接状态
"""

import hashlib
import requests
import time
from datetime import datetime

print("="*60)
print("微信云托管连接测试")
print("="*60)

# 微信云托管 URL
base_url = "https://flask-enou-237504-9-1414979075.sh.run.tcloudbase.com"
callback_url = f"{base_url}/stream_run"

print(f"\n测试 URL: {callback_url}\n")

# 微信 Token
token = "xingtuai2026"

# 构造验证参数
timestamp = str(int(time.time()))
nonce = "test_nonce"
echostr = "test_echostr"

# 生成签名
tmp_list = [token, timestamp, nonce]
tmp_list.sort()
tmp_str = ''.join(tmp_list)
signature = hashlib.sha1(tmp_str.encode()).hexdigest()

print(f"验证参数：")
print(f"  Token: {token}")
print(f"  Timestamp: {timestamp}")
print(f"  Nonce: {nonce}")
print(f"  Echostr: {echostr}")
print(f"  计算签名: {signature}")

# 构造完整 URL
test_url = f"{callback_url}?signature={signature}&timestamp={timestamp}&nonce={nonce}&echostr={echostr}"

print(f"\n完整测试 URL: {test_url}\n")

# 发送请求
print("正在发送请求...\n")

try:
    response = requests.get(test_url, timeout=10)

    print(f"响应状态码: {response.status_code}")
    print(f"响应头:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")

    print(f"\n响应内容: {response.text}")

    # 验证结果
    if response.status_code == 200:
        if response.text == echostr:
            print(f"\n{'='*60}")
            print("✅ 测试成功！微信验证接口正常工作！")
            print(f"{'='*60}\n")
            print("下一步：")
            print("1. 确认微信公众号配置的 URL 为:")
            print(f"   {callback_url}")
            print("2. 确认微信公众号配置的 Token 为:")
            print(f"   {token}")
            print("3. 在微信公众号中发送测试消息")
            exit(0)
        else:
            print(f"\n{'='*60}")
            print("⚠️ 验证失败！")
            print(f"{'='*60}\n")
            print(f"预期返回: {echostr}")
            print(f"实际返回: {response.text}")
            exit(1)
    else:
        print(f"\n{'='*60}")
        print("❌ 请求失败！")
        print(f"{'='*60}\n")
        print(f"状态码: {response.status_code}")
        exit(1)

except requests.exceptions.Timeout:
    print(f"\n{'='*60}")
    print("❌ 请求超时！")
    print(f"{'='*60}\n")
    print("可能的原因：")
    print("1. 服务未启动")
    print("2. 网络连接问题")
    exit(1)

except requests.exceptions.ConnectionError as e:
    print(f"\n{'='*60}")
    print("❌ 连接失败！")
    print(f"{'='*60}\n")
    print(f"错误信息: {e}")
    print("\n可能的原因：")
    print("1. URL 错误")
    print("2. 服务未启动")
    print("3. 防火墙阻止")
    exit(1)

except Exception as e:
    print(f"\n{'='*60}")
    print("❌ 测试失败！")
    print(f"{'='*60}\n")
    print(f"错误信息: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
