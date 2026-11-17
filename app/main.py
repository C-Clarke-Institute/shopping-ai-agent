from fastapi import FastAPI

from app.api.routes.chat import router as chat_router

app = FastAPI(title="AI Customer Support",
              description="AI powered customer support system using Langgraph",
              version="1.0.0")

app.include_router(chat_router)

def health_check():

    return {
        "status" : "success",
        "message" : "AI Agent is running"
    }