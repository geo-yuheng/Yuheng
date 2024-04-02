import os
from .const import YUHENG_CORE_NAME, YUHENG_VERSION
from .environment import get_yuheng_path
from hellologger import get_logger

log_config_local = {"foo": "bar"}
log_config_aliyun = {
    "LOG_CONFIG_ALIYUN_ENDPOINT": "cn-qingdao.log.aliyuncs.com",
    "LOG_CONFIG_ALIYUN_PROJECT": "yuhenglog",
    "LOG_CONFIG_ALIYUN_LOGSTORE": "dev",
}

logger = get_logger(
    log_path=os.path.join(get_yuheng_path(), "log"),
    log_file="log_{time}.log",
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
fence_length = 30
logger.info("[Yuheng] Start logging!")
logger.debug(
    "\n"
    + ("=" * fence_length + "\n")
    + "[Yuheng] Environment Info!\n"
    + ("=" * fence_length + "\n")
    + f"YUHENG_CORE_NAME    : {YUHENG_CORE_NAME}\n"
    + f"YUHENG_VERSION      : {YUHENG_VERSION}\n"
    + ("=" * fence_length + "\n")
)
