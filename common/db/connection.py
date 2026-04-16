import sqlite3

def get_connection():
    """
    SQLite 데이터베이스 connection 생성
    """
    return sqlite3.connect("chatbot.db")