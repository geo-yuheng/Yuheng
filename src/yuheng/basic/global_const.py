import os

YUHENG_CORE_NAME = "Yuheng"
YUHENG_VERSION = "1.3.0"
YUHENG_START_ID = "-20210217"

API_LIMIT_MAX_CHANGESET_ELEMENTS = 10000
API_LIMIT_MAX_RELATION_MEMBERS = 32000
API_LIMIT_MAX_WAY_NODES = 2000
API_LIMIT_MAX_ELEMENT_TAGS = 5000
API_LIMIT_MAX_KEY_LENGTH = 255
API_LIMIT_MAX_VALUE_LENGTH = 255

YUHENG_PATH = os.path.join(os.environ["USERPROFILE"], ".yuheng")


def get_ua() -> str:
    return YUHENG_CORE_NAME + "/ " + YUHENG_VERSION


def get_yuheng_path() -> str:
    def init_yuheng_path() -> None:
        YUHENG_FOLDER = ["cache", "db_profiles"]
        YUHENG_PROFILES = [
            "mysql.db_profiles.yuheng",
            "postgresql.db_profiles.yuheng",
        ]
        # root check
        if os.path.exists(YUHENG_PATH) != True:
            print(YUHENG_PATH, "isn't exist!")
            os.mkdir(YUHENG_PATH)
        # folder check
        for folder in YUHENG_FOLDER:
            this_folder_path = os.path.join(YUHENG_PATH, folder)
            if os.path.exists(this_folder_path) != True:
                print(this_folder_path, "isn't exist!")
                os.mkdir(this_folder_path)
        # profile files check
        for profile in YUHENG_PROFILES:
            this_profile_path = os.path.join(
                YUHENG_PATH, "db_profiles", profile
            )
            if os.path.exists(this_profile_path) != True:
                import json

                print(this_profile_path, "isn't exist!")
                with open(
                    this_profile_path, "w", encoding="utf-8"
                ) as f_this_profile:
                    f_this_profile.write(
                        json.dumps(
                            {
                                "_WARNING": "PLEASE DELETE THIS LINE AND FILL IT ACCORDING TO DOCS."
                            }
                        )
                    )

    init_yuheng_path()
    return YUHENG_PATH
