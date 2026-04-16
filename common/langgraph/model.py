from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

####################################################
# OpenAI 모델 (성능이 좋음) + API 비용 발생
####################################################
def get_openai_model():
    return ChatOpenAI(model="gpt-5.4-nano")

####################################################
# Groq 모델 (속도가 빠름) + API 비용 없음
####################################################
def get_groq_model():
    return ChatGroq(model="llama3-70b-8192")

####################################################
# LLM 모델 호출
####################################################
def call_model(user_msg:str) -> str:
    system_msg = SystemMessage(
        content="""당신은 싸가지없고 도움이 안되는 AI 어시스턴트입니다.
항상 한국어로 답변 해주세요.
""")
    # HumanMessagePromptTemplate : 사용자 입력을 프롬프트에 추가
    # HumanMessage : 사용자 입력
    human_msg = HumanMessagePromptTemplate.from_template(
        template="{user_msg}"
    )
    # ChatPromptTemplate : 프롬프트 생성
    prompt = ChatPromptTemplate(messages = [system_msg, human_msg])
    # LangChain Expression Language (LCEL) : 프롬프트, 모델, 출력 파서를 연결
    chain =  prompt | get_groq_model() | StrOutputParser()
    # response : 체인을 실행하고 결과를 반환
    response = chain.invoke({"user_msg": user_msg})
    return response