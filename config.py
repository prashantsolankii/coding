import os
import logging
from dotenv import load_dotenv

load_dotenv(".env")

db_config = {
    "DB_HOST": os.getenv('DB_HOST'),
    "DB_USER": os.getenv('DB_USER'),
    "DB_PASSWORD": os.getenv('DB_PASSWORD'),
    "DB_NAME": os.getenv('DB_NAME'),
    "LOG_LEVEL": os.getenv("LOG_LEVEL", logging.INFO), 
    "LOG_FILE": os.getenv("LOG_FILE", "basic.log")  
}

def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        level=db_config.get("LOG_LEVEL", "INFO"),  
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(db_config.get("LOG_FILE"))  
        ]
    )
    return logging.getLogger(__name__)