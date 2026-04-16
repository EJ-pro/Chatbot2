####################################################
# 환경변수 등록
####################################################
from dotenv import load_dotenv

load_dotenv()

####################################################
# Streamlit 애플리케이션
####################################################
import streamlit as st
from common.screen.display import print_message
from common.screen.histstory import init_history
from common.langgraph.run import response_from_graph

st.title("챗봇")

####################################################
# session_state 초기화 및 저장된 메시지 출력
# common/screen/histstory.py에 구현
####################################################
init_history()

####################################################
# 사용자 질문 입력 및 assistant 답변 화면 출력
# common/screen/display.py에 구현
####################################################
question = st.chat_input("질문을 입력해주세요")

if question is not None:
    # 사용자 질문을 session_state에 추가
    user_msg = {
        "role": "user",
        "content": question
    }
    st.session_state.messages.append(user_msg) # session_state에 추가
    print_message(**user_msg) # 화면에 출력

    # assistant 답변을 session_state에 추가
    response = response_from_graph(user_msg["content"])
    ai_msg = {
        "role": "assistant",
        "content": response
    }
    st.session_state.messages.append(ai_msg) # session_state에 추가
    print_message(**ai_msg) # 화면에 출력