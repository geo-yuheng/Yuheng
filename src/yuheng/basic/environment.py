import os

from .const import YUHENG_CORE_NAME, YUHENG_VERSION


def get_yuheng_path() -> str:
    YUHENG_PATH = os.path.join(os.environ["USERPROFILE"], ".yuheng")

    def init_yuheng_path() -> None:
        YUHENG_FOLDER = ["cache", "db_profiles", "log"]
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
                                "yuheng_doctype": "db_profile",
                                "_WARNING": "PLEASE DELETE THIS LINE AND FILL IT ACCORDING TO DOCS.",
                            }
                        )
                    )

    init_yuheng_path()
    return YUHENG_PATH


def get_ua() -> str:
    return YUHENG_CORE_NAME + "/ " + YUHENG_VERSION
