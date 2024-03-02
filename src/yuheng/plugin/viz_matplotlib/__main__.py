import os
import sys

import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.component import Node, Relation, Way


def init(
    width: int, height: int, N: float, W: float, S: float, E: float, **kwargs
):
    """
    需要计算画布对应的坐标范围
    这意味着我们只能当作地球是平面的，任何方向每个像素间的距离对应的经纬度变化都是均一的。但球面并非如此。
    如果要按照几何距离来计算，请用distance_NS和distance_WE
    """
    range_NS = abs(N - S)
    range_WE = abs(W - E)

    dpi = 100
    figsize = (width, height)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    plt.plot([1, 2, 3, 4])
    plt.xlabel("经度")
    plt.ylabel("纬度")

    plt.show()

    pass


def main() -> None:
    print("This plugin can't be run as module.")


if __name__ == "__main__":
    main()
