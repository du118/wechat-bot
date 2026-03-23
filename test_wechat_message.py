#!/usr/bin/env python3
"""
测试微信消息收发
"""

import requests
import time

SERVER_URL = 'http://127.0.0.1:80/stream_run'

def generate_xml_message(from_user, to_user, content):
    """生成微信消息 XML"""
    create_time = str(int(time.time()))
    xml = f"""<xml>
<ToUserName><![CDATA[{to_user}]]></ToUserName>
<FromUserName><![CDATA[{from_user}]]></FromUserName>
<CreateTime>{create_time}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{content}]]></Content>
</xml>"""
    return xml

def test_text_message():
    """测试文本消息"""
    print("="*60)
    print("测试文本消息")
    print("="*60)

    from_user = 'o1234567890'  # 用户 openid
    to_user = 'gh_test123'     # 公众号原始ID
    content = '你好'            # 用户消息

    xml_data = generate_xml_message(from_user, to_user, content)

    print(f"\n发送消息：")
    print(f"  FromUser: {from_user}")
    print(f"  ToUser: {to_user}")
    print(f"  Content: {content}")

    print(f"\nXML 数据：")
    print(xml_data)

    try:
        response = requests.post(
            SERVER_URL,
            data=xml_data.encode('utf-8'),
            headers={'Content-Type': 'application/xml'},
            timeout=30  # 增加超时时间，AI可能需要更长时间
        )

        print(f"\n响应状态码：{response.status_code}")
        print(f"响应内容：")
        print(response.text)

        if response.status_code == 200:
            print("\n✅ 消息发送成功！")
            return True
        else:
            print("\n❌ 消息发送失败！")
            return False

    except requests.exceptions.Timeout:
        print("\n⚠️ 请求超时（AI处理可能需要更长时间）")
        return False
    except Exception as e:
        print(f"\n❌ 请求失败：{e}")
        return False

def test_image_message():
    """测试图片消息"""
    print("\n" + "="*60)
    print("测试图片消息")
    print("="*60)

    from_user = 'o1234567890'
    to_user = 'gh_test123'
    create_time = str(int(time.time()))

    xml_data = f"""<xml>
<ToUserName><![CDATA[{to_user}]]></ToUserName>
<FromUserName><![CDATA[{from_user}]]></FromUserName>
<CreateTime>{create_time}</CreateTime>
<MsgType><![CDATA[image]]></MsgType>
<PicUrl><![CDATA[http://example.com/image.jpg]]></PicUrl>
<MediaId><![CDATA[media_id_12345]]></MediaId>
</xml>"""

    print(f"\n发送图片消息")

    try:
        response = requests.post(
            SERVER_URL,
            data=xml_data.encode('utf-8'),
            headers={'Content-Type': 'application/xml'},
            timeout=30
        )

        print(f"\n响应状态码：{response.status_code}")
        print(f"响应内容：")
        print(response.text)

        if response.status_code == 200:
            print("\n✅ 图片消息处理成功！")
            return True
        else:
            print("\n❌ 图片消息处理失败！")
            return False

    except Exception as e:
        print(f"\n❌ 请求失败：{e}")
        return False

if __name__ == '__main__':
    print("\n" + "="*60)
    print("开始测试微信消息收发")
    print("="*60 + "\n")

    # 测试文本消息
    test_text_message()

    # 等待一下
    time.sleep(2)

    # 测试图片消息
    test_image_message()

    print("\n" + "="*60)
    print("测试完成！")
    print("="*60)
