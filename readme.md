# OSMChina-Keqing_sword
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword?ref=badge_shield)


A non-database Python base OSM data parser, with SQL operation simulated 

----------

本项目是一个基于Python的对`.osm`文件的访问库

## 技术细节和文件

### kqs_class.py

OSM数据对象库

### kqs_crud.py

模拟数据库操作行为，不过只有查是可以批量的，增删只能单id，改是增删组合 ~~省事~~

## Pypy friendly

This package don't depend on any package, so it's compatible with latest pypy.

## 命名来源

项目Leader @Jyunhou 钦点

[![](https://avatars.githubusercontent.com/u/45530478?v=4)](https://zh.wikipedia.org/wiki/%E5%8E%9F%E7%A5%9E%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8#%E7%92%83%E6%9C%88%E4%B8%83%E6%98%9F)

## NOT

列举出可能与本项目相近，相似，但目的并非一致的替代品

### Dump Reader

+ https://github.com/osmcode/osmium （我们有参考）
+ https://github.com/openstreetmap/osmosis
+ https://gitlab.com/osm-c-tools/osmctools (osmconvert)

### Data process framework

+ https://github.com/gboeing/osmnx （我们有参考）
+ https://github.com/iandees/pyosm

### Query SQL or DSL

+ https://github.com/drolbr/Overpass-API （我们有参考）
+ https://github.com/sqlalchemy/sqlalchemy

### Database

+ osm2pgsql
+ osm2pgrouting
+ osm2mysql, osm2mongo, and so on.

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword?ref=badge_large)
