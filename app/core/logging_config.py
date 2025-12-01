import logging
import logging.config
import os
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "standard": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        },
        "json": {
            "format": (
                '{"time": "%(asctime)s", "level": "%(levelname)s", '
                '"logger": "%(name)s", "message": "%(message)s"}'
            )
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
            "stream": "ext://sys.stdout",
        },
        "file_info": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "standard",
            "filename": "logs/info.log",
            "when": "midnight",
            "backupCount": 10,     # keeps 10 days of logs
            "level": "INFO",
        },
        "file_error": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "json",
            "filename": "logs/error.log",
            "when": "midnight",
            "backupCount": 30,     # keeps 30 days of logs
            "level": "ERROR",
        },
    },

    "loggers": {
        "": {  # root logger
            "handlers": ["console", "file_info", "file_error"],
            "level": "INFO",
            "propagate": False
        },
        "uvicorn.error": {
            "level": "INFO",
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
    },
}
