# README

Here are requirement and guideline for developers.

## Proper variable name

We now ask you to use more clear and meaningful variable name.

Especially for some basic OSM related property, you may want to name them with similar name in OSM, but unfortunately they are reserved by python. Such as:
* `map` (use "carto" instead)
* `type` (use "element_type" or other similar instead)

## "Kill that o-ta-ku"

Still many place using the name "Waifu" for main class.

We suggest this usage:

```python
import yuheng

world=yuheng.Carto()
```

or

```python
from yuheng import Carto

world=Carto()
```