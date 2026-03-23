#!/usr/bin/env python3
"""
测试微信验证请求
"""

import hashlib
import time
import random
import requests

# 微信配置
WECHAT_TOKEN = 'xingtuai2026'
SERVER_URL = 'http://127.0.0.1:80/stream_run'

def generate_signature(token, timestamp, nonce):
    """生成微信签名"""
    params = [token, timestamp, nonce]
    params.sort()
    tmp_str = ''.join(params)
    signature = hashlib.sha1(tmp_str.encode()).hexdigest()
    return signature

def test_verification():
    """测试微信验证"""
    print("="*60)
    print("开始测试微信验证请求")
    print("="*60)

    # 生成随机参数
    timestamp = str(int(time.time()))
    nonce = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    echostr = '1234567890'

    # 计算签名
    signature = generate_signature(WECHAT_TOKEN, timestamp, nonce)

    print(f"\n发送参数：")
    print(f"  signature: {signature}")
    print(f"  timestamp: {timestamp}")
    print(f"  nonce: {nonce}")
    print(f"  echostr: {echostr}")

    # 发送请求
    url = f"{SERVER_URL}?signature={signature}&timestamp={timestamp}&nonce={nonce}&echostr={echostr}"

    print(f"\n请求URL：")
    print(f"  {url}")

    try:
        response = requests.get(url, timeout=5)
        print(f"\n响应状态码：{response.status_code}")
        print(f"响应内容：{response.text}")

        if response.status_code == 200 and response.text == echostr:
            print("\n✅ 验证成功！")
            return True
        else:
            print("\n❌ 验证失败！")
            return False

    except Exception as e:
        print(f"\n❌ 请求失败：{e}")
        return False

def test_invalid_signature():
    """测试无效签名"""
    print("\n" + "="*60)
    print("测试无效签名")
    print("="*60)

    # 生成随机参数
    timestamp = str(int(time.time()))
    nonce = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    echostr = '1234567890'

    # 使用错误的签名
    signature = 'invalid_signature_12345'

    print(f"\n发送参数：")
    print(f"  signature: {signature}")
    print(f"  timestamp: {timestamp}")
    print(f"  nonce: {nonce}")
    print(f"  echostr: {echostr}")

    url = f"{SERVER_URL}?signature={signature}&timestamp={timestamp}&nonce={nonce}&echostr={echostr}"

    try:
        response = requests.get(url, timeout=5)
        print(f"\n响应状态码：{response.status_code}")
        print(f"响应内容：{response.text}")

        if response.status_code == 401:
            print("\n✅ 正确拒绝无效签名！")
            return True
        else:
            print("\n❌ 应该返回 401！")
            return False

    except Exception as e:
        print(f"\n❌ 请求失败：{e}")
        return False

if __name__ == '__main__':
    # 测试有效签名
    test_verification()

    # 测试无效签名
    test_invalid_signature()
