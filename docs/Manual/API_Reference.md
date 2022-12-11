# API Reference

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

