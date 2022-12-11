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

But in some kind of overpass-api response the `version` will be erased, that's because you only need `body` information for its shape, not whole `meta`. Currently Keqing can't support this kind of data.

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

Keqing offer 3 kind of basic OSM element types, they are `Node`, `Way` and `Relation`, and they are inherited from super class `BaseOsmModel`(which will be replaced with `Base` in future version).

They can be found in `src/kqs/type_element.py`.

You may also found another 2 type prefixed file `type_data.py` and `type_constraint.py`, in most cases you won't need them if you don't want to handle history data or audit member role in relation.

### `Node`

Here is prototype of `Node`:

### `Way`

Here is prototyoe of `Way`:

### `Relation`:

Here is prototype of `Relation`:

## Method

I have a great way to present it but there is a character limit and I can't write it

By Fermat
