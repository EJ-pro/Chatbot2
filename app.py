import streamlit as st
from common.screen.display import print_message
from common.screen.histstory import init_history

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
    msg = {
        "role": "user",
        "content": question
    }
    st.session_state.messages.append(msg) # session_state에 추가
    print_message(**msg) # 화면에 출력

    # assistant 답변을 session_state에 추가
    msg = {
        "role": "assistant",
        "content": "답변"
    }
    st.session_state.messages.append(msg) # session_state에 추가
    print_message(**msg) # 화면에 출력

