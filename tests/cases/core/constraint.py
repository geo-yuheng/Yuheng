import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..", "src")
sys.path.append(src_dir)

import yuheng
from yuheng import Bounds

Bounds(
    {
        "minlat": "11.4514",
        "maxlat": "8",
        "minlon": "-10",
        "maxlon": "19.19",
        "origin": "NONE SENSE",
    }
)

# 输入
# WW:-EE是(NN,SS)
# 输入
# WW,SS,EE,NN
