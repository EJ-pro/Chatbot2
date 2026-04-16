from langgraph.graph import add_messages
from typing import Annotated
from typing_extensions import TypedDict

# Annotated : 타입 힌트를 추가하는 함수
# add_messages : 메시지를 상태에 추가하는 함수
# TypedDict : 딕셔너리의 키와 값을 정의하는 함수

################################################
# 상태 정의
################################################
class ChatbotState(TypedDict):
    """
    LangGraph의 상태를 정의하는 딕셔너리
    """
    messages: Annotated[list, add_messages]