import json
import os

KQS_VERSION: str = json.load(
    open(os.path.join(os.path.dirname(__file__), "global_const.json"), "r")
)["KQS_VERSION"]
KQS_CORE_NAME: str = json.load(
    open(os.path.join(os.path.dirname(__file__), "global_const.json"), "r")
)["KQS_CORE_NAME"]
# 👴和刻晴小姐的结婚纪念日🥰
KQS_START_ID: int = json.load(
    open(os.path.join(os.path.dirname(__file__), "global_const.json"), "r")
)["KQS_START_ID"]
