import logging
import sys
from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter("[%(levelname)s] %(asctime)s  — %(message)s")
log_file = "my_app.log"


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(log_file)
    file_handler.setFormatter(formatter)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = True
    return logger