#!/usr/bin/env python3
"""
测试两个 Token，看看服务到底用的是哪个
"""

import hashlib
import requests
import time

print("="*60)
print("测试两个 Token")
print("="*60)

base_url = "https://flask-enou-237504-9-1414979075.sh.run.tcloudbase.com/stream_run"

# 两个 Token
tokens = {
    "xingtuai2026": "xingtuai2026",  # 旧 Token
    "xingtulai2026": "xingtulai2026",  # 新 Token
}

for token_name, token_value in tokens.items():
    print(f"\n{'='*60}")
    print(f"测试 Token: {token_name}")
    print(f"{'='*60}\n")

    # 构造验证参数
    timestamp = str(int(time.time()))
    nonce = "test_nonce"
    echostr = "test_echostr"

    # 生成签名
    tmp_list = [token_value, timestamp, nonce]
    tmp_list.sort()
    tmp_str = ''.join(tmp_list)
    signature = hashlib.sha1(tmp_str.encode()).hexdigest()

    test_url = f"{base_url}?signature={signature}&timestamp={timestamp}&nonce={nonce}&echostr={echostr}"

    print(f"Token: {token_value}")
    print(f"计算签名: {signature}\n")

    # 发送请求
    try:
        response = requests.get(test_url, timeout=10)

        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}\n")

        if response.status_code == 200 and response.text == echostr:
            print(f"✅ 这个 Token 是正确的！")
            print(f"\n{'='*60}")
            print(f"✅ 服务正在使用的 Token: {token_name}")
            print(f"{'='*60}\n")
            break
        else:
            print(f"❌ 这个 Token 不正确\n")

    except Exception as e:
        print(f"❌ 测试失败：{e}\n")
