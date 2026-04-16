from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

from common.langgraph.graph import create_chatbot_graph

################################################
# LangGraph 실행
################################################
def response_from_graph(user_msg:str) -> str:
    chat_graph = create_chatbot_graph()
    response = chat_graph.invoke({"messages":[HumanMessage(content=user_msg)]})
    return response["messages"][-1].content