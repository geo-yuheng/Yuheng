import re
from typing import List

import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)

from yuheng.basic import logger


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


def parse_header(header: str) -> dict:
    condition_list = re.findall(
        r"(?<![way|node|relation|nw|wr|nr|nwr])\[(.*?)\]", header
    )
    header_parameter = {}
    for condition in condition_list:
        key, value = tuple(condition.split(":"))
        header_parameter[key] = value
    return header_parameter


def parse_geocode(query_slice: str):
    return "★" + query_slice + "☆"


def parse_arrow(query_slice: str) -> List[str]:
    return [
        sub_query_slice.strip() for sub_query_slice in query_slice.split("->")
    ]


def get_query_parts(query_content: str) -> List[str]:
    query_parts = list(
        filter(
            bool,
            split_semicolon(remove_linebreak(remove_comment(query_content))),
        )
    )
    return query_parts


@logger.catch()
def parse(query_parts: List[str]) -> list:
    # 根据特征匹配来判断执行何种parse
    for i in range(len(query_parts)):
        if query_parts[i] == "":
            continue
        if (
            i == 0
            and re.findall(
                r"(?<![way|node|relation|nw|wr|nr|nwr])\[(.*?)\]",
                query_parts[0],
            )
            != []
        ):
            query_parts[0] = parse_header(query_parts[0])
            continue
        if "->" in query_parts[i]:
            query_parts[i] = parse_arrow(query_parts[i])
        if query_parts[i] == ")":
            brackets_pos = i - 1
            # print("[brackets_pos]", brackets_pos)
            while brackets_pos >= 0:
                # print("[brackets_pos].inloop", brackets_pos)
                # print("[brackets_pos].inloop.part", query_parts[brackets_pos])

                if query_parts[brackets_pos][0] != "(":
                    brackets_pos -= 1
                    continue
                else:
                    bracket_sub_query_parts = []
                    for j in range(brackets_pos, i + 1):
                        if j == brackets_pos:
                            bracket_sub_query_parts.append("(")
                            bracket_sub_query_parts.append(
                                query_parts[j].replace("(", "").strip() + ";"
                            )
                        elif j == i:
                            bracket_sub_query_parts.append(")")
                        else:
                            bracket_sub_query_parts.append(
                                query_parts[j].strip() + ";"
                            )
                    query_parts[brackets_pos] = "".join(
                        bracket_sub_query_parts
                    )
                    for j in range(brackets_pos + 1, i + 1):
                        query_parts[j] = ""
                    break
            query_parts[brackets_pos] = parse(
                get_query_parts(query_parts[brackets_pos][1:-1])
            )
    for i in range(len(query_parts)):
        if "geocodeArea" in query_parts[i] or "searchArea" in query_parts[i]:
            query_parts[i] = parse_geocode(query_parts[i])
    for i in range(len(query_parts)):
        if isinstance(query_parts[i], list):
            query_parts[i] = parse(query_parts[i])
    return query_parts
