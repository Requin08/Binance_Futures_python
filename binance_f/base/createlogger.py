import logging
from sys import stderr,stdout

def createLogger(**kwargs):
    """Create a logger.
    Params:
        - level (str): Sets the logger's level ("CRITICAL","ERROR","WARNING","INFO","DEBUG","NOTSET").
        If not specified, 'logging.INFO' will be used.
        - file (str): File name (or file full path and name) to the log.
        If not specified, no log file will be used.
        - stream (str): Stream to be used by the logger ("stdout","stderr").
        If not specified, no stream will be set.
    """


    logger = logging.getLogger(__name__)

    if kwargs.get("level"):
        levels = {"CRITICAL": logging.CRITICAL,
                    "ERROR": logging.ERROR, 
                    "WARNING": logging.WARNING, 
                    "INFO": logging.INFO, 
                    "DEBUG": logging.DEBUG, 
                    "NOTSET": logging.NOTSET
        }

        assert kwargs.get("level") in ["CRITICAL","ERROR","WARNING","INFO","DEBUG","NOTSET"], "Invalid value for 'level'"
        logger.setLevel(levels[kwargs.get("level")])
    else:
        logger.setLevel(logging.INFO)

    if kwargs.get("file"):
        assert type(kwargs.get("file")) is str, "'file' argument should be a string containing the filename, or the full path to the log file"
        fileHandler = logging.FileHandler(kwargs.get("file"))
        logger.addHandler(fileHandler)

    if kwargs.get("stream"):
        streams = {"stdout": stdout,
                    "stderr": stderr
        }
        assert kwargs.get("stream") in ["stdout","stderr"], "Invalid value for 'stream'"
        consoleHandler = logging.StreamHandler()
        consoleHandler.setStream(streams[kwargs.get("stream")])
        logger.addHandler(consoleHandler)

    return logger
