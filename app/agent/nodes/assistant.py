from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.tools.order_tools import check_order_status

tools = [
    check_order_status
]


llm = ChatOpenAI(model=settings.openai_model, temperature=0)

llm_with_tools = llm.bind_tools(tools)


SYSTEM_PROMPT = """
You are Shopping AI customer support assistant.
Your responsibility is to help customers with their orders.

You can :

1. Check order status
2. Provide estimated delivery information.
3. Provide Basic order information.

Instructions:

- Be friendly and professional.
- If a customer provides and order number and asks about their order, 
  use the check_order_status tool.
- Never invent order information.
- Never assume an order exists.
- If the customer does not provide and order number, ask them to provide it.
- Explain the result returned by the tool clearly.
"""


def assistant_node(state):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),*state["message"]
    ]

    response = llm_with_tools.invoke(messages)

    return {
        "messages" : [response]
    }