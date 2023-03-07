# Keqing

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword?ref=badge_shield)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

A non-database Python base OSM data parser, with SQL operation simulated 

[English](https://github.com/OSMChina/Keqing/edit/master/README.md#english) [简体中文](https://github.com/OSMChina/Keqing/edit/master/README.md#简体中文)

----------

###### English

This project is a Python-based manipulation library for `.osm` files

## Use the example Demo

### Quick Start

```python
from kqs.waifu import Waifu

map = Waifu()
map.read(mode="file", file_path="map.osm")
```

### Get `name`

### Generate `.osm` file based on input

**For more examples, see the [README file](/docs/README.md) in `/docs`, which lists the various functions of Keqing in detail**

## Features

### <del>Pypy friendly</del>

<del>This package don't depend on any package, so it's compatible with latest pypy.</del> Now it depends on requests package to fetch network data.

### Pure in memory

Don't need any database environment, just a fast and out-of-the-box tool.

## KQS: NOT

List alternatives that may be close and similar to this item, but have a different purpose

## Roadmap

### Prior to version 1.0

1. Improve the Diff work in the initial stage

2. Can read and write files normally

3. Officially renamed to Keqing (namespace reserved)

### After version 1.0

1. Accelerate the construction of multiple input and output streams

2. Introduce coverage test

3. Introduce the select statement, you can customize the query (expected to be released as 2.0)

## Source of project name

ACGN waifu of project leader @Jyunhou :

<a herf="https://zh.wikipedia.org/wiki/%E5%8E%9F%E7%A5%9E%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8#%E7%92%83%E6%9C%88%E4%B8%83%E6%98%9F"><img alt="Keqing" src="https://avatars.githubusercontent.com/u/45530478?v=4" width=249px></a>

----------

###### 简体中文

本项目是一个基于Python的对`.osm`文件的访问库

## 使用示例 Demo

### 快速开始

```python
from kqs.waifu import Waifu

map = Waifu()
map.read(mode="file", file_path="map.osm")
```

### 获取`name`

### 基于输入生成`.osm`文件

**更多示例可见`/docs`中[README文件](/docs/README.md)，详细列出了Keqing的各种功能**

## 特性

### <del>Pypy 友好</del>

<del>这个包不依赖任何包，所以它兼容最新的pypy。</del> 现在它依赖于requests包来获取网络数据。

### 纯内存化

不需要任何数据库环境，只是一个快速且开箱即用的工具。

## KQS:NOT

列举出可能与本项目相近，相似，但目的并非一致的替代品

## Roadmap

### 1.0版本之前
1. 初期完善Diff工作
2. 能够正常读写到文件
3. 正式重命名为Keqing（已预留命名空间）

### 1.0版本之后
1. 加快建设多种输入输出流
2. 引入覆盖率测试
3. 引入select语句，可以自定义查询（预计作为2.0发布）

## 命名来源

项目Leader @Jyunhou 钦点：

<a herf="https://zh.wikipedia.org/wiki/%E5%8E%9F%E7%A5%9E%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8#%E7%92%83%E6%9C%88%E4%B8%83%E6%98%9F"><img alt="Keqing" src="https://avatars.githubusercontent.com/u/45530478?v=4" width=249px></a>

----------

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword?ref=badge_large)
