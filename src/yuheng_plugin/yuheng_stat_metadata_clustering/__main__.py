import argparse
import os
import sys
import datetime
import zoneinfo
from typing import Tuple, Dict
from collections import Counter, OrderedDict

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.basic import logger
from yuheng.component import Node, Way, Relation


LOCAL_TIMEZONE = "Asia/Shanghai"


def main(**kwargs):
    # if run in standalone cli, only support input a xml file and then parse it to Carto
    # if run by import, both parse xml or pass Carto object is acceptable.
    for k, v in kwargs.items():
        logger.debug(v)

        if isinstance(v, str):
            # parse mode
            if v[0:5] != "<?xml":
                # this is a file path
                logger.debug("this is a file path")
                logger.info(v)
                world = Carto()
                world.read(mode="file", file_path=v)
            else:
                logger.debug("this is a text")
                world = Carto()
                world.read(mode="memory", text=v)
        elif isinstance(v, type(Carto())):
            world = v
            world.meow()
        else:
            logger.info(f'Unrecognizable value from key "{k}"')
            pass

        def get_metadata_frame_raw(world: Carto) -> Tuple[str, int, int, int]:
            metadata_frame_raw = []
            for id, element in world.node_dict.items():
                metadata_frame_raw.append(
                    (
                        "n" + str(element.id),
                        element.timestamp,
                        element.uid,
                        element.changeset,
                    )
                )
            for id, element in world.way_dict.items():
                metadata_frame_raw.append(
                    (
                        "w" + str(element.id),
                        element.timestamp,
                        element.uid,
                        element.changeset,
                    )
                )
            for id, element in world.relation_dict.items():
                metadata_frame_raw.append(
                    (
                        "r" + str(element.id),
                        element.timestamp,
                        element.uid,
                        element.changeset,
                    )
                )
            return metadata_frame_raw

        def get_metadata_frame(
            metadata_frame_raw: Tuple[str, int, int, int]
        ) -> Dict[str, str]:
            metadata_frame = []  # 因为暂时不引入pandas所以用字典做行，用了pandas就直接行数组插入了。
            for element in metadata_frame_raw:
                timezone_server = datetime.timezone.utc
                timezone_user = zoneinfo.ZoneInfo(LOCAL_TIMEZONE)
                time_utc_str = element[1]
                time_utc = datetime.datetime.strptime(
                    time_utc_str, "%Y-%m-%dT%H:%M:%SZ"
                )
                time_utc = time_utc.replace(tzinfo=timezone_server)
                time_user = time_utc.astimezone(timezone_user)

                metadata_frame.append(
                    {
                        "id": element[0],
                        "uid": str(element[2]),
                        "changeset": str(element[3]),
                        "time_year": time_user.year,
                        "time_month": time_user.month,
                        "time_day": time_user.day,
                        "time_hour": time_user.hour,
                        "time_minute": time_user.minute,
                        "time_second": time_user.second,
                    }
                )
            return metadata_frame

        metadata_frame_raw = get_metadata_frame_raw(world)
        metadata_frame = get_metadata_frame(metadata_frame_raw)
        del metadata_frame_raw
        logger.debug(metadata_frame[0])
        logger.debug(f"len(metadata_frame)={len(metadata_frame)}")

        # clustering_uid = {}
        clustering_year = Counter(
            element.get("time_year") for element in metadata_frame
        )
        clustering_year = dict(OrderedDict(sorted(clustering_year.items())))

        logger.debug(clustering_year)
        logger.info(len(clustering_year))

        import seaborn as sns
        import matplotlib.pyplot as plt

        # 将字典转换为适合绘图的数据结构
        years = list(clustering_year.keys())
        counts = list(clustering_year.values())

        # 使用 seaborn 来创建一个条形图
        sns.set(style="whitegrid")  # 设置 seaborn 的样式
        plt.figure(figsize=(10, 8))  # 设置图形的大小
        sns.barplot(x=years, y=counts, palette="viridis")  # 创建条形图并设置调色板

        plt.title("Yearly Distribution of Elements")  # 设置图表标题
        plt.xlabel("Year")  # 设置 x 轴标签
        plt.ylabel("Count")  # 设置 y 轴标签
        plt.xticks(rotation=45)  # 旋转 x 轴上的标签，使之更容易阅读

        plt.show()  # 显示图表


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--file", type=str, default=True, dest="file")
    main(**argument_parser.parse_args().__dict__)
