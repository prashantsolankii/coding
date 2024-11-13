from sqlalchemy import create_engine,URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys_path
from config import db_config,setup_logging

class DatabaseConnection():
    def __init__(self):
        self.logger = setup_logging()
        self.url = URL.create(
            "mysql+mysqlconnector",
            username = db_config.get('DB_USER'),
            password = db_config.get('DB_PASSWORD'),
            port = db_config.get('DB_PORT'),
            host = db_config.get('DB_HOST'),
            database = db_config.get('DB_NAME')
        )
        self.engine = create_engine(self.url)
        self.sessionlocal = sessionmaker(
            autocommit = False,
            autoflush=False,
            bind = self.engine
        )

        self.base = declarative_base()
    
    def create_tables(self):
        """Create all tables in database"""
        self.base.metadata.create_all(self.engine)
    
    def get_session(self):
        """Create and return a new session"""
        self.logger.info("Session has been started")
        return self.sessionlocal()

    def close_session(self,session):
        """Close the session"""
        if session:
            session.close()
            self.logger.info("Session has been closed")
        