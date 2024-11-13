import sys_path
from sqlalchemy import DateTime,Column,Integer,String
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy.orm import DeclarativeBase
from typing import List
from databaseconnection import DatabaseConnection
from sqlalchemy import String
from datetime import datetime

db_manager = DatabaseConnection()
base = db_manager.base

class User(base):
    __tablename__ = 'user_account'

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(30),nullable=False)
    email:Mapped[str] = mapped_column(String(20),unique=True,nullable=False)
    password:Mapped[str] = mapped_column(String(20),nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)

