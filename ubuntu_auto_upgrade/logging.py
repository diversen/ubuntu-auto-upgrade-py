import os
import logging
from logging.handlers import RotatingFileHandler
from config import CONFIG


def configure_app_logging():

    log_level = CONFIG["log_level"]
    log_directory = "logs"
    log_filename = "main.log"

    os.makedirs(log_directory, exist_ok=True)
    log_file_path = os.path.join(log_directory, log_filename)

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Create handlers
    file_handler = RotatingFileHandler(
        log_file_path, maxBytes=1048576, backupCount=5
    )  # 1MB per file, with backup up to 5 files
    stream_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_handler.setFormatter(logging.Formatter(log_format))
    stream_handler.setFormatter(logging.Formatter(log_format))

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
