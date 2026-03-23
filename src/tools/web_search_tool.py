from langchain.tools import tool
from langchain.tools import ToolRuntime
from coze_coding_dev_sdk import SearchClient
from coze_coding_utils.runtime_ctx.context import new_context


def _execute_web_search(query: str, count: int = 10, time_range: str = "1w") -> str:
    """执行联网搜索的内部函数（实时性优化版）"""
    ctx = new_context(method="search.web")
    client = SearchClient(ctx=ctx)

    try:
        # 优化搜索查询：添加实时性关键词
        enhanced_query = query
        time_keywords = ["最新", "2024", "2025", "今天", "本周", "本月", "近期", "最近"]

        # 如果查询中不包含时间关键词，自动添加
        if not any(kw in query for kw in time_keywords):
            enhanced_query = f"{query} 最新 2024 2025"

        # 使用search方法，添加时间范围和AI摘要
        response = client.search(
            query=enhanced_query,
            search_type="web_summary",
            count=count,
            time_range=time_range,  # 默认搜索最近1周
            need_summary=True,
            need_url=True
        )

        result_parts = []

        # 添加搜索说明
        result_parts.append(f"【实时搜索 - 最近{time_range}】")
        result_parts.append(f"搜索词：{enhanced_query}\n")

        if response.summary:
            result_parts.append(f"📌 AI智能摘要\n{response.summary}\n")

        if response.web_items:
            result_parts.append(f"📊 搜索结果（共{len(response.web_items)}条）\n")

            # 按时间排序（最新的在前）
            sorted_items = sorted(
                response.web_items,
                key=lambda x: x.publish_time or "",
                reverse=True
            )

            for idx, item in enumerate(sorted_items, 1):
                publish_time = item.publish_time if item.publish_time else "时间未知"

                result_parts.append(
                    f"{idx}. {item.title}\n"
                    f"   📅 {publish_time}\n"
                    f"   🌐 {item.site_name}\n"
                    f"   🔗 {item.url}\n"
                    f"   📝 {item.snippet[:180]}...\n"
                )
        else:
            result_parts.append("未找到相关结果，建议调整搜索关键词或扩大时间范围。")

        return "\n".join(result_parts)
    except Exception as e:
        return f"搜索失败: {str(e)}"


@tool
def web_search(query: str, count: int = 10, time_range: str = "1w", runtime: ToolRuntime = None) -> str:
    """实时联网搜索（已优化时效性）。

    用于获取最新的资讯、行业动态、技术前沿、政策法规、市场数据等信息。
    自动添加实时性关键词，确保搜索结果是最新的。

    Args:
        query: 搜索关键词或问题
        count: 返回结果数量，默认10条，建议5-15条
        time_range: 时间范围，默认"1w"（最近一周），可选值：
            - "1d": 最近1天
            - "1w": 最近1周（推荐）
            - "1m": 最近1个月
            - "3m": 最近3个月

    Returns:
        返回按时间排序的实时搜索结果，包含AI摘要、发布时间、来源和链接

    Example:
        web_search("AI最新趋势", time_range="1d")  # 搜索最近1天
        web_search("星途纪元AI", time_range="1w")  # 搜索最近1周
    """
    return _execute_web_search(query, count, time_range)
