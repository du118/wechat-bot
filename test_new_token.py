#!/usr/bin/env python3
"""
测试新的 Token: xingtulai2026
"""

import hashlib
import requests
import time

print("="*60)
print("测试新 Token: xingtulai2026")
print("="*60)

# 微信云托管 URL
base_url = "https://flask-enou-237504-9-1414979075.sh.run.tcloudbase.com"
callback_url = f"{base_url}/stream_run"

# 新的 Token
token = "xingtulai2026"

# 构造验证参数
timestamp = str(int(time.time()))
nonce = "test_nonce"
echostr = "test_echostr"

# 生成签名
tmp_list = [token, timestamp, nonce]
tmp_list.sort()
tmp_str = ''.join(tmp_list)
signature = hashlib.sha1(tmp_str.encode()).hexdigest()

test_url = f"{callback_url}?signature={signature}&timestamp={timestamp}&nonce={nonce}&echostr={echostr}"

print(f"\n测试 URL: {test_url}")
print(f"Token: {token}")
print(f"计算签名: {signature}\n")

# 发送请求
print("正在发送请求...\n")

try:
    response = requests.get(test_url, timeout=10)

    print(f"响应状态码: {response.status_code}")
    print(f"响应内容: {response.text}\n")

    if response.status_code == 200 and response.text == echostr:
        print(f"{'='*60}")
        print("✅ Token 验证成功！新 Token 正常工作！")
        print(f"{'='*60}\n")
        exit(0)
    else:
        print(f"{'='*60}")
        print("❌ Token 验证失败！")
        print(f"{'='*60}\n")
        print(f"预期返回: {echostr}")
        print(f"实际返回: {response.text}")
        exit(1)

except Exception as e:
    print(f"❌ 测试失败：{e}")
    exit(1)
