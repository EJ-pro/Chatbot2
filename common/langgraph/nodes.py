from common.langgraph.state import ChatbotState
from common.langgraph.model import get_groq_model

################################################
# 노드 정의
################################################
def chatbot_node(state: ChatbotState) -> ChatbotState:
    model = get_groq_model()
    response = model.invoke(state["messages"][-1].content)
    return {
        **state,
        "messages":[response]
    }