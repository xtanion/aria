import sys
import logging
from colorlog import ColoredFormatter

def get_logger(name="esp32_server"):
    formatter = ColoredFormatter(
        fmt="%(log_color)s[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        log_colors={
            "DEBUG":    "cyan",
            "INFO":     "green",
            "WARNING":  "yellow",
            "ERROR":    "red",
            "CRITICAL": "bold_red",
        },
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger
