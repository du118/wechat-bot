#!/usr/bin/env python3
"""
测试微信公众号消息处理功能
"""

import requests
from datetime import datetime

print("="*60)
print("微信公众号消息处理测试")
print("="*60)

# 微信云托管 URL
callback_url = "https://flask-enou-237504-9-1414979075.sh.run.tcloudbase.com/stream_run"

# 模拟微信消息 XML
wechat_message_xml = """<xml>
<ToUserName><![CDATA[gh_test123]]></ToUserName>
<FromUserName><![CDATA[ouser123]]></FromUserName>
<CreateTime>1742785482</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[你好]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>"""

print(f"\n测试 URL: {callback_url}")
print(f"\n模拟消息: 你好")
print(f"消息类型: text\n")

# 发送 POST 请求
print("正在发送 POST 请求...\n")

try:
    response = requests.post(
        callback_url,
        data=wechat_message_xml.encode('utf-8'),
        headers={'Content-Type': 'application/xml'},
        timeout=30
    )

    print(f"响应状态码: {response.status_code}")
    print(f"\n响应内容:\n{response.text}\n")

    # 验证结果
    if response.status_code == 200:
        # 检查是否返回 XML 格式的回复
        if '<xml>' in response.text:
            print(f"{'='*60}")
            print("✅ 消息处理成功！AI 正常回复！")
            print(f"{'='*60}\n")

            # 尝试提取回复内容
            try:
                import xml.etree.ElementTree as ET
                root = ET.fromstring(response.text)
                reply_content = root.find('Content').text
                print(f"AI 回复内容:\n{reply_content}\n")
            except:
                pass

            print("结论：微信公众号和微信云托管已成功连接！")
            print("现在可以在微信公众号中发送消息进行测试。")
            exit(0)
        else:
            print(f"{'='*60}")
            print("⚠️ 返回内容格式异常")
            print(f"{'='*60}\n")
            print(f"返回内容: {response.text}")
            exit(1)
    else:
        print(f"{'='*60}")
        print(f"❌ 请求失败！状态码: {response.status_code}")
        print(f"{'='*60}\n")
        print(f"响应内容: {response.text}")
        exit(1)

except requests.exceptions.Timeout:
    print(f"{'='*60}")
    print("❌ 请求超时！")
    print(f"{'='*60}\n")
    print("可能的原因：")
    print("1. AI 响应时间过长")
    print("2. 网络连接问题")
    print("3. 服务正在处理中")
    exit(1)

except requests.exceptions.ConnectionError as e:
    print(f"{'='*60}")
    print("❌ 连接失败！")
    print(f"{'='*60}\n")
    print(f"错误信息: {e}")
    exit(1)

except Exception as e:
    print(f"{'='*60}")
    print("❌ 测试失败！")
    print(f"{'='*60}\n")
    print(f"错误信息: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
