# GanyuQL

## 语法设计

### 集合 **set**

通过花括号来代表符合`()`内约束条件的集合体。`{()}` 是没有任何有效约束条件的全集。

集合可以被命名。

在第一次声明一个集合的时候就可以通过`{foo: ()}`来将其命名为`{foo}`。集合的命名和约束可以同时进行。

集合也可在运算时被命名，如`{(A)}->railway/.railway`就代表一个名为`{railway}`的集合。

当使用一个已被定义的集合时，我们应使用`{set_name}`来使用。

### 约束条件 **constraint**

所有约束条件可以以`[][][]`并列。

诸如`[rail=yes]`的属于以标签定义的约束条件。

同样应该支持OverpassQL的`areaname`、`poly`、`bbox`等约束条件

同样应该支持OverpassQL的CSV输出描述等约束条件。它可以用于约束输出，这类约束条件应当需要在`$()`内排列。

### 运算 **operator**

对于需要提取为集合可能仍保留`>`算符？还是说干脆显式一点

* `{(A)}->{(B)}`代表集合提取，并得到一个集合
* `{(A)}=>(B)`代表按照某种条件操作，并终结整个语句，得到不可变集合。

这样上述两个语法混用可以得到 `{{(A)}->.railway}=>([rail=yes])`

因此一个传递链中只能包含一次`=>`。

### 输入和输出 **stream**

执行完`->`运算得到的集合仍可参与运算或输出。
执行完`=>`运算后此时的集合将不可继续变化。只能输出。
要得到输出到屏幕或控制台或API，应输出到stdout中。
输入默认为全集`{()}`。
输出默认为空集`{$}`。输出可以被约束条件限制，记为`{$()}`。

## 语言特性设计

### 抗缩进与抗猫性

文件开头和结尾分别需要添加`{**`与`**}`进行包装，以确定有效的代码内容。当然这并非强制的，当未能解析到这两个令牌组合的时候，应将整个文件都视为代码。对于能通过最前的`{**`和最接近前述`{**`的`**}`所包裹的内容，应视为代码。

代码中含有多个运算链（传递链、推导链）时，不同的运算链之间应以`;`隔开。不推荐在一个文件中同时存在多个运算链。

### 注释

注释采用python风格的`#`作为注释的开端，但因为是QL语句，就势必会遇到折行和缩进的问题，因此在考虑通过`#**#`的方式定义行内注释。而多行注释可以认为是一个行内注释，依然按照`#**#`来进行注释。这样和js/cpp风格的注释唯一不同就在于token的不同了。

### 简略输入输出

当传递链不以`{()}`开头的时候，自动添加这一起始集合。当传递链没有输出的时候给出建议，用户应用建议即可添加`=>{$()}`，否则就输出空集（因为GanyuQL应允许不存在输出，但不允许不存在输入）。

## 与OverpassQL的异同

不用进行`>`这样的操作去提取一个集合体了，也不用`>,railway`之类的方式进行运算