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
            "access_key_id": os.environ.get("ALIYUN_ACCESSKEY_ID"),
            "access_key": os.environ.get("ALIYUN_ACCESSKEY_SECRET"),
            "project": "yuhenglog",
            "log_store": "dev",
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
logging_handler_aliyun = logging.getLogger("sls").handlers[0]

loguru_config = {}
loguru_format = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}"
logger = loguru_logger

# local-file
logger.add(
    sink=os.path.join(get_yuheng_path(), "log", "log_{time}.log"),
    format=loguru_format,
    level="TRACE",
    **loguru_config
)
# saas_aliyun_sls
logger.add(
    sink=logging_handler_aliyun,
    format=loguru_format,
    level="INFO",
    **loguru_config
)
# saas_aws_cloudwatch
# logger.add(sink=logging_handler_aws) # WIP
# clickhouse
# logger.add(sink=logging_handler_clickhouse) # WIP
# elasticsearch
# logger.add(sink=logging_handler_elasticsearch) # WIP
# syslog stream
# # Read https://docs.render.com/log-streams#sumo-logic
# webhook
# # discord/slack/telegram_bot

# logger.disable("yuheng")
logger.info("loguru enabled")
