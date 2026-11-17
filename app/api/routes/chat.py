import logging

from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage

from app.Schemas.chat import ChatRequest, ChatResponse
from app.agent.graphs.order_graph import order_graph

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api",tags=["AI Customer Support"])

@router.post("/chat", response_model=ChatResponse)
def chat(request : ChatRequest):

    try :

        #converts customer input into a Langchain message
        user_message = HumanMessage(content=request.message)

        # Execute Langgraph
        result = order_graph.invoke({"messages" : [user_message]})

        #retrieve the final message
        final_message = result["messages"][-1]

        return ChatResponse(
            answer=str(final_message.content)
        )

    except Exception:

        logger.exception("Error while porcessing chat request")

        raise HTTPException(status_code=500, detail="Unable to process your message. Please try again.")








