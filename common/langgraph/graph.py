from langgraph.graph import StateGraph,START, END
from common.langgraph.nodes import chatbot_node
from common.langgraph.state import ChatbotState
from common.db.checkpointer import get_checkpointer

################################################
# 그래프 생성
################################################
def create_chatbot_graph(is_checkpointer:bool=True):
    # 그래프 정의
    graph = StateGraph(ChatbotState)
    # 노드 추가
    graph.add_node("chatbot_node", chatbot_node)
    # 엣지 추가
    graph.add_edge(START, "chatbot_node")
    graph.add_edge("chatbot_node", END)
    # 그래프 컴파일
    if is_checkpointer:
        return graph.compile(checkpointer=get_checkpointer())
    # LangGraph Studio용
    return graph.compile()