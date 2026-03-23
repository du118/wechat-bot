import base64
import os
import requests
from langchain.tools import tool, ToolRuntime
from coze_coding_dev_sdk import TTSClient, ASRClient
from coze_coding_utils.runtime_ctx.context import new_context


@tool
def speech_to_text(audio_url: str = None, base64_data: str = None, runtime: ToolRuntime = None) -> str:
    """语音识别（ASR）：将语音转换为文字。

    支持通过URL或Base64编码的音频数据进行语音识别。

    Args:
        audio_url: 音频文件的URL地址（与base64_data二选一）
        base64_data: Base64编码的音频数据（与audio_url二选一）
        支持格式：WAV/MP3/OGG OPUS/M4A
        限制：时长≤2小时，大小≤100MB

    Returns:
        返回识别出的文字内容

    Example:
        通过URL识别:
        speech_to_text(audio_url="https://example.com/audio.mp3")

        通过Base64识别:
        speech_to_text(base64_data="data:audio/mp3;base64,...")
    """
    ctx = new_context(method="asr.recognize")
    client = ASRClient(ctx=ctx)

    try:
        uid = runtime.context.user_id if runtime and runtime.context else "default_user"

        if audio_url:
            text, data = client.recognize(uid=uid, url=audio_url)
        elif base64_data:
            # 移除可能的data URI前缀
            if "," in base64_data:
                base64_data = base64_data.split(",", 1)[1]
            text, data = client.recognize(uid=uid, base64_data=base64_data)
        else:
            return "错误：必须提供 audio_url 或 base64_data 参数"

        result = data.get("result", {})
        duration = result.get("duration", 0)

        return f"【语音识别结果】\n识别内容：{text}\n音频时长：{duration / 1000:.2f}秒"
    except Exception as e:
        return f"语音识别失败：{str(e)}"


@tool
def text_to_speech(text: str, speaker: str = "zh_female_xiaohe_uranus_bigtts", runtime: ToolRuntime = None) -> str:
    """文字转语音（TTS）：将文字转换为语音。

    支持多种语音风格和音效调节。

    Args:
        text: 要合成的文字内容（必填）
        speaker: 语音ID，可选值：
            - zh_female_xiaohe_uranus_bigtts（默认，小荷，通用）
            - zh_female_vv_uranus_bigtts（薇薇，中英双语）
            - zh_male_m191_uranus_bigtts（云舟，男声）
            - zh_male_taocheng_uranus_bigtts（小天，男声）
            - zh_male_dayi_saturn_bigtts（大亦，配音）
            - zh_female_mizai_saturn_bigtts（米崽，配音）
        可选高级参数（当前不暴露）：
            - speech_rate: 语速调节（-50到100）
            - loudness_rate: 音量调节（-50到100）

    Returns:
        返回音频文件的下载链接

    Example:
        text_to_speech(text="欢迎使用星途纪元AI助手")
        text_to_speech(text="Hello, welcome!", speaker="zh_female_vv_uranus_bigtts")
    """
    ctx = new_context(method="tts.synthesize")
    client = TTSClient(ctx=ctx)

    try:
        uid = runtime.context.user_id if runtime and runtime.context else "default_user"

        audio_url, audio_size = client.synthesize(
            uid=uid,
            text=text,
            speaker=speaker,
            audio_format="mp3",
            sample_rate=24000
        )

        return f"【语音合成成功】\n音频URL：{audio_url}\n文件大小：{audio_size / 1024:.2f}KB\n\n💡 提示：点击链接即可播放或下载"
    except Exception as e:
        return f"语音合成失败：{str(e)}"
