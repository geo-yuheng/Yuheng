import os
import logging.config

from loguru import logger as loguru_logger

from .global_const import get_yuheng_path

logging_config = {
    "version": 1,
    "formatters": {
        "rawformatter": {"class": "logging.Formatter", "format": "%(message)s"}
    },
    "handlers": {
        "sls_handler": {
            "()": "aliyun.log.QueuedLogHandler",
            "level": "INFO",
            "formatter": "rawformatter",
            "end_point": "cn-qingdao.log.aliyuncs.com",
            "access_key_id": "",
            "access_key": "",
            "project": "yuhenglog",
            "log_store": "loggggggggggg",
        }
    },
    "loggers": {
        "sls": {
            "handlers": [
                "sls_handler",
            ],
            "level": "INFO",
            "propagate": False,
        }
    },
}
logging.config.dictConfig(logging_config)
logging_handler_sls = logging.getLogger("sls").handlers[0]

loguru_config = {"level": "INFO"}
loguru_format = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}"
logger = loguru_logger


# file
logger.add(
    sink=os.path.join(get_yuheng_path(), "log", "log_{time}.log"),
    format=loguru_format,
    **loguru_config
)
# aliyun sls
logger.add(sink=logging_handler_sls, format=loguru_format, **loguru_config)
# clickhouse
# logger.add(sink=logging_handler_clickhouse)
# openobserve
# logger.add(sink=logging_handler_openobserve)

# logger.disable("yuheng")
logger.info("loguru enabled")
