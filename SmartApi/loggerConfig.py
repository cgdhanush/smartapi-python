import logging
import os

LOG_DIR = "logs"
LOG_FILE = "app.log"

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str, level: str = "WARNING") -> logging.Logger:
    """
    Creates and returns a logger instance that logs messages at the specified level and above.
    Logs are saved in logs/app.log and also printed to console.

    Parameters:
        name (str): Logger name.
        level (str): Logging level (e.g. 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
                     Defaults to 'WARNING'.

    Returns:
        logging.Logger: Configured logger instance.
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.WARNING))

    if not logger.hasHandlers():
        # File handler
        log_path = os.path.join(LOG_DIR, LOG_FILE)
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(getattr(logging, level.upper(), logging.WARNING))

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, level.upper(), logging.WARNING))

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
