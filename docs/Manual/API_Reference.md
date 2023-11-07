# API Reference

## Model

### General

Currently we have 2 base model, `BaseOsmModel` and `Base`, this aspect of abstract is  because many element in OSM have similar structure. For historical data we need to allow multi different version been storaged in same place.

The most difference between them are diff method, we extract every method about diff from base model, because specific calculation may have vary widely depending on the source.

### Mandatory part

#### Standard

In a extracted OSM raw file you can see this attribute in XML element:

```xml
<type id="1"
     visible="true"
     version="1"
     changeset="1"
     timestamp="1970-01-01T00:00:00Z"
     user="string"
     uid="1"/>
```

**Those attributes are vital to a element:**

+ `id` and `version` is the only identifier of a OSM element if type was given.

But in some kind of overpass-api response the `version` will be erased, that's because you only need `body` information for its shape, not whole `meta`. Currently Yuheng can't support this kind of data.

**Those attributes are not such vital but also useful so almost all kinds of backend contain them:**

+ `changeset` is given, although if you have whole database you can query all changeset's data found where this version's element was modified, but that costs too much.
+ `timestamp`
+ `user` and `uid`, this help you found who made it, even this user delete its account or changed name you can use `uid` as identifier. ~~But who cares?~~~

#### JOSM extened

And if this was extracted by JOSM, you will see this:
```xml
<type action="delete"/>
```
JOSM use this tag simulate OSC file, because OSC file emphasize on what changed, and changes can be catagorized with **create**, **modify** and **delete**, only those 3 kinds.

#### Spatial data

if this is a node, it was expected to carrying spatial information, so those 2 attribute will be mandatory:

```xml
<node lat=""
      lon=""/>
```

## Type

### General

Yuheng offer 3 kind of basic OSM element types, they are `Node`, `Way` and `Relation`, and they are inherited from super class `BaseOsmModel`(which will be replaced with `Base` in future version).

They can be found in `src/kqs/type_element.py`.

You may also found another 2 type prefixed file `type_data.py` and `type_constraint.py`, in most cases you won't need them if you don't want to handle history data or audit member role in relation.

### `Node`

Prototype of`Node` had inherited from [`Base` model](#Model). But as mentioned above, if you want to create a new Node object, you need to specify its lat and lon when construct.

```python
    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str]):
        super().__init__(attrib, tag_dict)
        if not attrib.get("lat") and not attrib.get("lon"):
            attrib["action"] = "delete"
        else:
            self.lat: float = float(attrib["lat"])
            self.lon: float = float(attrib["lon"])
            self.__lat_backup: float = float(attrib["lat"])
            self.__lon_backup: float = float(attrib["lon"])
```
Here are other method prototype:

#### `__str__`

WELCOME TO CONTRIBUTE!

#### `has_diff`

tldr

#### `__has_position_diff`

tldr

#### `get_tag_all`

tldr

#### `get_tag_query`

The difference with `get_tag_all` is this method need you pass a overpass query or working Ganyu query sentence.

#### `get_upstream_way`

Detail about this function can be found in https://github.com/OSMChina/Yuheng/issues/5

#### `get_upstream_relation`

Detail about this function can be found in https://github.com/OSMChina/Yuheng/issues/5

#### `is_latest`

See comment

#### `find_latest`

See comment inside code

#### `find_history`

See comment inside code

### `Way`

Here is prototyoe of `Way`:

### `Relation`:

Here is prototype of `Relation`:

## Method

I have a great way to present it but there is a character limit and I can't write it

By Fermat
