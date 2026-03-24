"""
微信公众号消息推送服务器
用于接收和处理微信公众号的消息
"""

from flask import Flask, request
import hashlib
import xml.etree.ElementTree as ET
from datetime import datetime
import os
import sys

# 添加项目路径到Python路径
# 确保 src 目录可以被正确导入
current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
project_root = os.path.dirname(current_dir)

# 添加项目根目录和 src 目录到路径
if project_root not in sys.path:
    sys.path.insert(0, project_root)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 微信公众号配置（需要在微信公众号后台配置的值）
WECHAT_TOKEN = 'xingtulai2026'  # 你在微信公众号后台填写的Token
WECHAT_AESKEY = ''  # 你的EncodingAESKey，如果生成了请填写

app = Flask(__name__)

@app.route('/stream_run', methods=['GET', 'POST'])
def wechat_callback():
    """微信公众号回调接口"""

    print(f"\n{'='*50}")
    print(f"收到请求：{request.method}")
    print(f"{'='*50}\n")

    # 处理微信服务器验证请求（GET）
    if request.method == 'GET':
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')

        print(f"验证请求参数：")
        print(f"  signature: {signature}")
        print(f"  timestamp: {timestamp}")
        print(f"  nonce: {nonce}")
        print(f"  echostr: {echostr}")

        # 验证签名
        if verify_signature(signature, timestamp, nonce):
            print(f"\n✅ 验证成功！返回echostr: {echostr}")
            return echostr  # 必须返回echostr，不能有其他内容
        else:
            print(f"\n❌ 验证失败！")
            return 'Invalid signature', 401

    # 处理消息推送（POST）
    elif request.method == 'POST':
        try:
            # 获取原始XML数据
            xml_data = request.data
            print(f"收到POST消息：\n{xml_data.decode('utf-8')}\n")

            # 解析XML
            root = ET.fromstring(xml_data)

            # 提取消息信息
            msg_type = root.find('MsgType').text
            from_user = root.find('FromUserName').text  # 用户openid
            to_user = root.find('ToUserName').text  # 公众号原始ID

            print(f"消息类型：{msg_type}")
            print(f"用户ID：{from_user}")
            print(f"公众号ID：{to_user}")

            # 处理文本消息
            if msg_type == 'text':
                content = root.find('Content').text
                print(f"用户消息：{content}")

                # 调用AI助手获取回复
                reply = get_ai_response(content, from_user)
                print(f"AI回复：{reply}")

                # 返回XML格式的回复
                response_xml = generate_text_reply(to_user, from_user, reply)
                print(f"返回给微信的XML：\n{response_xml}\n")

                return response_xml

            # 处理图片消息
            elif msg_type == 'image':
                pic_url = root.find('PicUrl').text
                print(f"用户发送了图片：{pic_url}")

                reply = "收到您的图片，星途纪元AI正在分析中..."
                response_xml = generate_text_reply(to_user, from_user, reply)

                return response_xml

            # 处理语音消息
            elif msg_type == 'voice':
                media_id = root.find('MediaId').text
                print(f"用户发送了语音，MediaID：{media_id}")

                reply = "收到您的语音，星途纪元AI正在识别中..."
                response_xml = generate_text_reply(to_user, from_user, reply)

                return response_xml

            # 其他消息类型
            else:
                reply = f"当前支持文本、图片、语音消息，您的消息类型：{msg_type}"
                response_xml = generate_text_reply(to_user, from_user, reply)

                return response_xml

        except Exception as e:
            print(f"\n❌ 处理消息失败：{str(e)}")
            import traceback
            traceback.print_exc()
            return 'Error', 500

def verify_signature(signature, timestamp, nonce):
    """验证微信签名"""
    # 1. 将token、timestamp、nonce三个参数进行字典序排序
    tmp_list = [WECHAT_TOKEN, timestamp, nonce]
    tmp_list.sort()

    # 2. 将三个参数字符串拼接成一个字符串进行sha1加密
    tmp_str = ''.join(tmp_list)
    hash_str = hashlib.sha1(tmp_str.encode()).hexdigest()

    print(f"签名验证：")
    print(f"  加密字符串：{tmp_str}")
    print(f"  计算签名：{hash_str}")
    print(f"  微信签名：{signature}")
    print(f"  结果：{'✅ 匹配' if hash_str == signature else '❌ 不匹配'}")

    # 3. 将加密后的字符串与signature对比
    return hash_str == signature

def generate_text_reply(to_user, from_user, content):
    """生成文本消息回复XML"""
    create_time = int(datetime.now().timestamp())

    xml_template = f'''<xml>
<ToUserName><![CDATA[{to_user}]]></ToUserName>
<FromUserName><![CDATA[{from_user}]]></FromUserName>
<CreateTime>{create_time}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{content}]]></Content>
</xml>'''

    return xml_template

def get_ai_response(user_message, user_id):
    """
    调用星途纪元AI助手获取回复
    """
    try:
        print(f"\n{'='*50}")
        print(f"开始调用AI助手...")
        print(f"用户消息：{user_message}")
        print(f"用户ID：{user_id}")
        print(f"{'='*50}\n")

        # 导入Agent
        from src.agents.agent import build_agent
        from langchain_core.messages import HumanMessage

        # 构建Agent实例
        agent = build_agent()

        # 调用AI
        response = agent.invoke(
            [HumanMessage(content=user_message)],
            config={"configurable": {"thread_id": user_id}}
        )

        print(f"\n{'='*50}")
        print(f"响应类型：{type(response)}")
        print(f"响应内容：{response}")
        print(f"{'='*50}\n")

        # 提取 AI 回复
        # LangGraph 返回的是 State 对象，需要从 messages 中提取 AI 的回复
        if hasattr(response, 'messages') and len(response.messages) > 0:
            # 获取最后一条 AI 回复消息
            from langchain_core.messages import AIMessage
            ai_messages = [msg for msg in response.messages if isinstance(msg, AIMessage)]

            if ai_messages:
                # 获取最后一条 AI 消息
                reply = ai_messages[-1].content
            else:
                # 如果没有 AI 消息，获取最后一条消息
                reply = response.messages[-1].content
        elif hasattr(response, 'content'):
            reply = response.content
        else:
            reply = str(response)

        print(f"\n{'='*50}")
        print(f"AI助手回复：{reply}")
        print(f"{'='*50}\n")

        return reply

    except Exception as e:
        error_msg = f"星途纪元AI暂时无法响应：{str(e)}"
        print(f"\n❌ AI调用失败：{error_msg}")
        import traceback
        traceback.print_exc()

        return error_msg

if __name__ == '__main__':
    print("\n" + "="*60)
    print("星途纪元AI - 微信公众号服务器启动中...")
    print("="*60 + "\n")

    print(f"Token配置：{WECHAT_TOKEN}")
    print(f"AESKey配置：{WECHAT_AESKEY or '未配置'}")

    # 使用环境变量中的 PORT，默认为 80
    port = int(os.environ.get('PORT', 80))

    print(f"监听地址：0.0.0.0:{port}")
    print(f"回调地址：https://kdq6mqbnnn.coze.site/stream_run")
    print("\n" + "="*60 + "\n")

    # 启动Flask服务器
    app.run(host='0.0.0.0', port=port, debug=True)
