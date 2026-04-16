from .connection import get_connection

from langgraph.checkpoint.sqlite import SqliteSaver

def get_checkpointer():
    """
    SqliteSaver 생성
    """
    return SqliteSaver(get_connection())

# 테이블 생성
# CREATE TABLE IF NOT EXISTS messages (
#     thread_id TEXT NOT NULL,
#     run_id TEXT NOT NULL,
#     step INTEGER NOT NULL,
#     name TEXT,
#     type TEXT,
#     data BLOB,
#     PRIMARY KEY (thread_id, run_id, step)
# );