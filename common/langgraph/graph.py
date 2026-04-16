from langgraph.graph import StateGraph, END
from common.langgraph.nodes import chatbot_node
from common.langgraph.state import ChatbotState

################################################
# 그래프 생성
################################################
def create_chatbot_graph():
    # 그래프 정의
    graph = StateGraph(ChatbotState)
    # 노드 추가
    graph.add_node("chatbot_node", chatbot_node)
    # 엣지 추가
    graph.add_edge("chatbot_node", END)
    # 그래프 컴파일
    return graph.compile()