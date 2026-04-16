from langchain_core.messages import SystemMessage, HumanMessage

from common.langgraph.graph import create_chatbot_graph
import streamlit as st

################################################
# LangGraph 실행
################################################
def response_from_graph(user_msg:str) -> str:
    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }
    chat_graph = create_chatbot_graph()
    response = chat_graph.invoke({"messages":[HumanMessage(content=user_msg)]},
    config=config
    )

    return response["messages"][-1].content