from fastapi import APIRouter

from app.rag.retriever import retrieve_context
from app.rag.retriever import retrieve_context
from app.rag.chat_prompts import build_chat_prompt
from app.rag.llm import generate_response

router = APIRouter()

@router.post("/chat")
def chat(data: dict):

    user_message = data.get("message", "").strip()

    if not user_message:
        return {"error": "Message cannot be empty"}

    context = retrieve_context(
        user_message,
        k=4
    )

    prompt = build_chat_prompt(
        user_message=user_message,
        context=context
    )

    response = generate_response(prompt)

    return {"response": response}
