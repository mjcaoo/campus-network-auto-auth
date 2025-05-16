import sys
import logging
from logging.handlers import RotatingFileHandler
from config import config

def setup_logging():
    """Configure logging for the application."""
    config["LOG_DIR"].mkdir(parents=True, exist_ok=True)
    
    # Create a rotating file handler with max 5 backup files
    file_handler = RotatingFileHandler(
        config["LOG_FILE"],
        maxBytes=5*1024*1024,  # 5MB per file
        backupCount=5,
        encoding="utf-8"
    )
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s",
        handlers=[
            file_handler,
            logging.StreamHandler(sys.stdout)
        ]
    ) 