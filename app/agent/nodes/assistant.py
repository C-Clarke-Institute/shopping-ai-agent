from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.tools.order_tools import check_order_status

tools = [
    check_order_status
]


llm = ChatOpenAI(model=settings.openai_model, temperature=0)

llm_with_tools = llm.bind_tools(tools)

