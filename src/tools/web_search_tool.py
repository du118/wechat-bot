from langchain.tools import tool
from langchain.tools import ToolRuntime
from coze_coding_dev_sdk import SearchClient
from coze_coding_utils.runtime_ctx.context import new_context


def _execute_web_search(query: str, count: int = 10) -> str:
    """执行联网搜索的内部函数"""
    ctx = new_context(method="search.web")
    client = SearchClient(ctx=ctx)

    try:
        response = client.web_search_with_summary(
            query=query,
            count=count
        )

        result_parts = []
        if response.summary:
            result_parts.append(f"【AI摘要】\n{response.summary}\n")

        if response.web_items:
            result_parts.append("【搜索结果】")
            for idx, item in enumerate(response.web_items, 1):
                result_parts.append(
                    f"\n{idx}. {item.title}\n"
                    f"   来源: {item.site_name}\n"
                    f"   链接: {item.url}\n"
                    f"   摘要: {item.snippet[:200]}..."
                )

        return "\n".join(result_parts) if result_parts else "未找到相关结果"
    except Exception as e:
        return f"搜索失败: {str(e)}"


@tool
def web_search(query: str, count: int = 10, runtime: ToolRuntime = None) -> str:
    """联网搜索实时信息。

    用于获取最新的资讯、行业动态、技术前沿、政策法规、市场数据等信息。

    Args:
        query: 搜索关键词或问题
        count: 返回结果数量，默认10条，建议5-15条

    Returns:
        返回搜索结果的摘要和详情，包含AI生成的摘要和网页链接
    """
    return _execute_web_search(query, count)
