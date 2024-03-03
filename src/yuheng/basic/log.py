from loguru import logger

log = logger
log.add(
    "file_{time}.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    level="INFO",
)
