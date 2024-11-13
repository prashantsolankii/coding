import sys_path
from models.user import User
from databaseconnection import DatabaseConnection
from sqlalchemy import select,update
from config import setup_logging

class UserManager:
    def __init__(self,get_session,close_session):
        self._get_session = get_session
        self._close_session = close_session
        self.logger = setup_logging()

    def login_user(self,email : str,password : str):
        try:
            with self._get_session() as session:
                if session:
                    stmt = select(User).where(User.email == email)
                    saved_output = session.scalar(stmt)
                    if not saved_output:
                        self.logger.info("No User found with this email:{email}")
                        self._close_session(session)
                        return False
                    if self.verify_password(password,saved_output.password):
                        self.logger.info(f"Welcome back, {saved_output.name}!")
                        self.update_password(email,session)
                        self._close_session(session)
                    else:
                        self.logger.info("Invalid Password for email : {email}")
                        self._close_session(session)
        except Exception as e:
            self.logger.error(f"Error {e} has occured")
            self._close_session(session)
            return False

    def verify_password(self,input_password : str,stored_password : str):
        """Verifies the provided password against the stored password""" 
        if input_password:   
            return input_password == stored_password
    
    def signup_user(self,name : str,email : str,password : str):
        new_user = User(
            name = name,
            email= email,
            password = password
        )
        try:
            with self._get_session()  as session:
                    if session:
                            session.add(new_user)
                            session.commit()
                            self.logger.info(f"User {name} has been added successfully")
                            self.update_password(email,session)
                            self._close_session(session)
                    else:
                        return False
        except Exception as e:
            session.rollback()
            self.logger.error(f"Error {e} occured during user registration")
            raise e
        
    def update_password(self,user_email,session):
        user_decision = input("Do you want to update your password(Y/N): ").upper().strip()
        if user_decision == 'Y':
            new_password = input("Please enter the new password: ").strip()
            if new_password:
                try:
                    stmt = update(User).where(User.email == user_email).values(password = str(new_password))
                    session.execute(stmt)
                    session.commit()
                    self.logger.info(f"password has been updated for {user_email}")
                except Exception as e:
                    self.logger.error(f"Error {e} has been occured")
                    self._close_session(session)
            else:
                self.logger.warning(f"Invalid choice for new_password by {user_email}")