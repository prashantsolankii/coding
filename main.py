import sys_path
from databaseconnection import DatabaseConnection
from controllers.usermanager import UserManager
from models.user import db_manager
import os
from views.consoleview import display_message

def get_input(prompt):
    """Get user input and check if it's not empty"""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty,Please try again!! ")
            continue
        return user_input

def main():
    """Main Entry point of the program"""

    user_manager = UserManager(db_manager.get_session,db_manager.close_session) 

    display_message("Application Started")

    while True:
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-2): ").strip()
        if choice == '1':
            name = get_input("Enter your name: ")
            email = get_input("Enter your email: ")
            password = get_input("Enter your password: ")
            user_manager.signup_user(name, email, password)
        elif choice == '2':
            email = get_input("Enter your email: ")
            password = get_input("Enter your password: ")
            user_manager.login_user(email, password)
        else:
            print("Exiting from the Application")
            break

if __name__ == "__main__":
    main()