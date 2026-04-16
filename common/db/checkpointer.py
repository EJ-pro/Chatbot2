from .connection import get_connection

from langgraph.checkpoint.sqlite import SQLiteSaver

def get_checkpointer():
    """
    SQLiteSaver 생성
    """
    return SQLiteSaver(connection=get_connection())