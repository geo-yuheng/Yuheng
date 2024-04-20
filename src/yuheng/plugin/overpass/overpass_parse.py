import re
from typing import List


def remove_comment(query_content: str) -> str:
    """
    注释移除有新的思想，块注释和行注释是可以互不相干的操作的。行注释并非找不到后置令牌，它的后置令牌就是\n，因为换行了就不再继续注释。
    因此注释就变为不贪婪的匹配最小的令牌包裹的段落，其中块注释匹配/*和*/之间作为注释体，行注释匹配//和\n之间作为注释体。
    移除注释就是对注释体进行替换的处理（对于匹配过程是后处理，但整个移除注释对于解析过程是预处理），不过处理方式不一样。
    块注释是直接替换为""，行注释则是替换为"\n"以保证这一行还在（虽然对于overpass来说是比较抗折行的不给\n也行，但毕竟最小程度降低对原来信息的改动）
    最后，可能还需要移除完全不存在任何内容的空行。因为这些空行可能是移除了注释造成的
    """
    pattern_line_comment = r"(//.*)"
    pattern_block_comment = r"(/\*.*?\*/)"

    # 移除块注释（/* ... */）
    query_content = re.sub(
        pattern_block_comment, "", query_content, flags=re.DOTALL
    )

    # 移除行注释（// ... \n）
    query_content = re.sub(
        pattern_line_comment, "\n", query_content, flags=re.MULTILINE
    )

    # 移除只包含空格或制表符的行和空行
    query_content = re.sub(r"^\s*$", "", query_content, flags=re.MULTILINE)
    query_content = "\n".join(list(filter(bool, query_content.split("\n"))))

    return query_content


def remove_linebreak(query_content: str) -> str:
    """
    移除所有换行符号便于分析与法
    """
    return query_content.replace("\n", "")


def split_semicolon(query_content: str) -> List[str]:
    """
    按照分号拆分不同部分，方便构建AST
    """
    query_parts = query_content.split(";")
    return query_parts


def parse(query_content: str) -> None:
    query_parts = split_semicolon(
        remove_linebreak(remove_comment(query_content))
    )
    print(query_parts)
