# 没写完呢还

# OSM 查询语言定义

该语言是为了**查询**本地`.osm`数据，
根据 [Overpass QL](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) 修改而成的玩具语言。

本语言是一个过程化，指令式的查询语言， 可以查询 Keqing_Sword 中一个 `Waifu` 对象中的 节点，路径和关系数据。

## 词法定义

将使用 [扩展巴科斯范式(EBNF)](https://zh.wikipedia.org/wiki/%E6%89%A9%E5%B1%95%E5%B7%B4%E7%A7%91%E6%96%AF%E8%8C%83%E5%BC%8F)
对语法进行定义：

```
statement = (out | query), `;` ;
```

### 基础常量

```
upper_case = `A` | `B` | `C` | `D` | `E` | `F` | `G`
              | `H` | `I` | `J` | `K` | `L` | `M` | `N`
              | `O` | `P` | `Q` | `R` | `S` | `T` | `U`
              | `V` | `W` | `X` | `Y` | `Z` ;
lower_case = `a` | `b` | `c` | `d` | `e` | `f` | `g`
              | `h` | `i` | `j` | `k` | `l` | `m` | `n`
              | `o` | `p` | `q` | `r` | `s` | `t` | `u`
              | `v` | `w` | `x` | `y` | `z` ;
char = upper_case | lower_case ;
digit = `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` ;
```

### 变量 (Item)

#### 变量名

变量名可以使用大小写英文字母，数字或下划线，但不得以数字开头。

```
item_name = (char | `_`), {char | digit | `_`} ;
```

#### 调用

全局变量 `._`

变量a `.a`

```
item = `.`, item_name ;
```

#### 赋值

`->.变量名`

```
assignment = `->`, item ;
```

### 输出语句 (Out)

将查询结果以 `List[BaseOsmModel]` 的形式返回

```
out = [`.`, var_name] out ;
```

### 查询 (Query)
可以是三种查询中的任意一种，结尾处可进行变量赋值
```
query = (tag_query | id_query | time_query), [assignment] ;
```

#### 标签查询

```
tag_query = entity_type, {`[`, condition, `]`} ;

entity_type = `node` | `way` | `rel` | `nwr` | `nw` | `wr` | `nr` ;
condition = cond_key_eq | cond_val_eq | cond_re

q_key = [`"`], key, [`"`] ;
q_value = `"`, val, `"` ;
re_key = `~`, re ;
re_val = `~`, re ;

key = (char | `_`), {char | digit | `_`} ;
val = ?? any valid unicode string ?? ;
re = `"`, ?? any regular expression ??, `"` ;
```

键（不）存在：

`["key"]`
`[!"key"]`

```
cond_key_eq = [`!`], q_key ;
```

按值（不）匹配：

`["key"="value"]`
`["key"!="value"]`

```
cond_val_eq = q_key, [`!`], `=`, q_val ;
```

按正则（不）匹配：

`["key"~"value"]`
`["key"!~"value"]`
`[~"key"~"value"]`
`[~"key"~"value",i]`

```
cond_re = (q_key | re_key), [`!`], (q_val | re_val), [`i`] ;
```

### ID查询

`WAY[{{ID}}=="114514"];`

// todo

### 时间戳查询

`NODE[{{TIME}}>=2021-10-01T11:11:11];`

// todo
