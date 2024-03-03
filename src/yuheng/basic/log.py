import os

from loguru import logger

from .global_const import get_yuheng_path


log_config = {"level": "INFO"}
log = logger
log.add(
    os.path.join(get_yuheng_path(), "log", "log_{time}.log"),
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    **log_config
)
