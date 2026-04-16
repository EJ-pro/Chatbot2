import streamlit as st
from common.screen.display import print_message

####################################################
# session_state 초기화 및 저장된 메시지 출력
####################################################
def init_history() -> None:
    """
    session_state 초기화 및 저장된 메시지 출력
    """
    if "messages" not in st.session_state:
        st.session_state.messages = [] # session_state에 messages가 없으면 초기화
    
    for message in st.session_state.messages: # session_state에 messages가 있으면 반복 출력
        # ** : 딕셔너리의 키와 값을 인자로 전달
        print_message(**message)