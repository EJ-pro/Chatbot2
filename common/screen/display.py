import streamlit as st

# role : user, assistant 구분
# content : 출력할 메시지
def print_message(role:str, content:str) -> None:
    """
    역할과 메시지를 입력받아 화면에 출력
    """
    with st.chat_message(role):
        st.markdown(content)