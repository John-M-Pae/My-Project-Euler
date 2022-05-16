"""
Template for logging the project.
"""
import logging

def project_logger() -> logging.log:
    """
    Returns the logger for the project, contains both file and stream handlers.
    """
    log = logging.getLogger("euler_logger")
    log.setLevel(logging.DEBUG)

    log.addHandler(project_file_handler())
    log.addHandler(project_stream_handler())

    return log

def project_file_handler() -> logging.FileHandler:
    """
    Provides a file handler at the the INFO level.

    log format:
        [%(filename)s:%(levelname)s] :: %(message)s
    """
    log_file = logging.FileHandler("euler_log.log")
    log_file.setLevel(logging.INFO)

    file_format = logging.Formatter('[%(filename)s:%(levelname)s] :: %(message)s')
    log_file.setFormatter(file_format)

    return log_file

def project_stream_handler() -> logging.StreamHandler:
    """
    Provides a stream handler at the DEBUG level.

    log format:
        [%(filename)s:%(lineno)d] :: %(message)s
    """
    log_stream = logging.StreamHandler('[%(filename)s:%(lineno)d] :: %(message)s')
    log_stream.setLevel(logging.DEBUG)

    stream_format = logging.Formatter()
    log_stream.setFormatter(stream_format)

    return log_stream