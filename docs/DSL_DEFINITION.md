# 没写完呢还

# OSM 查询语言定义

该语言是为了**查询**本地`.osm`数据，
根据 [Overpass QL](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) 修改而成的玩具语言。

本语言是一个过程化，指令式的查询语言， 可以查询 Keqing_Sword 中一个 `Waife` 对象中的 节点，路径和关系数据。

## 词法定义

将使用 [扩展巴科斯范式(EBNF)](https://zh.wikipedia.org/wiki/%E6%89%A9%E5%B1%95%E5%B7%B4%E7%A7%91%E6%96%AF%E8%8C%83%E5%BC%8F)
对语法进行定义：

```
query = ????;
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
char = upper_case | lower_case
digit = `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` ;
```

### 变量名

变量名可以使用大小写英文字母，数字或下划线，但不得以数字开头。

```
var_name = (char | `_`), {char | digit | `_`};
```

### 赋值

`[->.变量名]`

```
assignment = `[`, `->`, `.`, var_name, `]`;
```

### 条件查询

```
entity_type = `node` | `way` | `rel`;
query = type, {`[`, condition, `]`};

condition = cond_key_eq | cond_val_eq | cond_re

re = `"`, ?? any regular expression ??, `"`;

q_key = [`"`], key, [`"`];
q_value = `"`, val, `"`;
re_key = `~`, re;
re_val = `~`, re;
```

["key"]            /* filter objects tagged with this key and any value */

[!"key"]           /* filter objects not tagged with this key and any value */

```
cond_key_eq = [`!`], q_key;
```

["key"="value"]    /* filter objects tagged with this key and this value */

["key"!="value"]   /* filter objects tagged with this key but not this value, or not tagged with this key */

```
cond_val_eq = q_key, [`!`], `=`, q_val;
```

["key"~"value"]    /* filter objects tagged with this key and a value matching a regular expression */

["key"!~"value"]   /* filter objects tagged with this key but a value not matching a regular expression */

[~"key"~"value"]   /* filter objects tagged with a key and a value matching regular expressions */

[~"key"~"value",i] /* filter objects tagged with a key and a case-insensitive value matching regular expressions */

```
cond_re = (q_key | re_key), [`!`], (q_val | re_val), [`i`];
```

### ID查询

### BBOX
```
bbox = `(`, box_south, `,`, box_west, `,`, box_north, `,`, box_east, `)`
box_south = ?? decimal, -90.0 ~ 90.0 ??
box_west  = ?? decimal, -180.0 ~ 180.0 ??
box_north = ?? decimal, -90.0 ~ 90.0 ??
box_east  = ?? decimal, -180.0 ~ 180.0 ??
```

### 块查询

```
block = union

union = 
```

### 时间语法

###