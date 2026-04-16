# 🤖 AI Multi-Agent Chatbot (Chatbot2)

LangGraph와 Streamlit을 활용한 강력한 멀티 에이전트 챗봇 시스템입니다. 현재 LLM 모델 연동 및 기본적인 채팅 인터페이스 구축이 완료되었습니다.

## ✨ 주요 기능

- **Multi-Model Support**: OpenAI(고성능) 및 Groq(고속/무료) 모델 선택적 활용 가능.
- **LCEL(LangChain Expression Language)**: 프롬프트, 모델, 출력 파서를 체인으로 연결하여 유연한 로직 구현.
- **Persistent Memory**: SQLite(준비 중) 및 Streamlit `session_state`를 통한 대화 문맥 유지.
- **Unfriendly Persona**: "싸가지없고 도움이 안 되는" 독특한 컨셉의 AI 어시스턴트 적용.
- **Intuitive UI**: Streamlit 기반의 현대적인 채팅 인터페이스.

## 🛠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Orchestration**: [LangChain](https://www.langchain.com/), [LangGraph](https://www.langchain.com/langgraph)
- **LLM Providers**: OpenAI, Groq
- **Environment**: Python-dotenv

## 📁 프로젝트 구조

```text
chatbot/
├── app.py                  # Streamlit 메인 실행 파일 (모델 연동 및 UI)
├── common/                 # 공용 모듈 및 기능
│   ├── langgraph/
│   │   └── model.py        # LLM 모델 정의 및 호출 로직 (Chain 구현)
│   ├── screen/
│   │   ├── display.py      # 메시지 렌더링 컴포넌트
│   │   └── histstory.py    # 대화 이력 관리 모듈
│   └── db/                 # (개발 예정) 데이터베이스 관리
├── .env                    # API 키 관리 (비공개)
├── .env.sample             # 환경 변수 설정 샘플
└── requirements.txt        # 의존성 패키지 목록
```

## 🚀 시작하기

### 1. 환경 설정 및 패키지 설치

```bash
uv venv .venv --python 3.13
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일을 생성하고 필요한 API 키를 입력합니다. (참고: `.env.sample`)

```bash
cp .env.sample .env
```

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

### 3. 애플리케이션 실행

```bash
streamlit run app.py
```

---

## 📝 주요 구현 상세

### 🧠 모델 연동 (`common/langgraph/model.py`)

- `ChatOpenAI`와 `ChatGroq`을 지원합니다.
- `ChatPromptTemplate`을 사용하여 시스템 명령(Persona)과 사용자 입력을 구조화합니다.
- `prompt | model | StrOutputParser()` 형태의 LCEL 체인을 통해 응답을 생성합니다.

### 🎨 인터페이스 (`app.py`, `common/screen/`)

- `st.chat_input`을 통해 사용자 입력을 받고, `call_model` 함수를 호출하여 AI 답변을 생성합니다.
- 모든 대화 기록은 `st.session_state`에 저장되어 세션 동안 유지됩니다.
