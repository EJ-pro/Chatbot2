import sqlite3

# "__"로 시작하는 변수는 외부에서 사용하지 않겠다는 의미
__sqlite_connection = None

def get_connection():
    """
    SQLite 데이터베이스 connection 생성
    """
    global __sqlite_connection
    if __sqlite_connection is None:
        __sqlite_connection = sqlite3.connect(
            "chatbot_memory.db",
            check_same_thread=False
        )
    return __sqlite_connection