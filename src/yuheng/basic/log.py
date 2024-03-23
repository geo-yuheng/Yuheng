from .global_const import get_yuheng_path
from hellologger import get_logger

log_config_local = {"foo": "bar"}
log_config_aliyun = {
    "LOG_CONFIG_ALIYUN_ENDPOINT": "cn-qingdao.log.aliyuncs.com",
    "LOG_CONFIG_ALIYUN_PROJECT": "yuhenglog",
    "LOG_CONFIG_ALIYUN_LOGSTORE": "dev",
}

logger = get_logger(
    log_path=get_yuheng_path(),
    log_target={
        "local": True,
        "aliyun": False,
        "aws": False,
    },
    log_level={
        "local": "TRACE",
        "aliyun": "INFO",
    },
    **{**log_config_local, **log_config_aliyun},
)
# logger.disable("yuheng")
logger.info("[Yuheng] Start logging!")
