import os

from loguru import logger

from .global_const import get_yuheng_path

logger_config = {"level": "INFO"}
logger_format = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}"
logger.add(
    os.path.join(get_yuheng_path(), "log", "log_{time}.log"),
    format=logger_format,
    **logger_config
)
