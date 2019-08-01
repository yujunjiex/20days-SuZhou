# coding: UTF-8
"""编写函数，接收字符串参数，返回一个列表，其中第一个元素为大写字母个数，第二个元素为小写字母个数"""


def capitalization_words(strs: str):
    """返回一个包含字符串中大写字母个数和小写字母个数的列表"""
    lower_count = len([s for s in map(str, strs) if s.islower()])
    upper_count = len([s for s in map(str, strs) if s.isupper()])
    return [lower_count, upper_count]


def _capitalization_words(strs: str):
    lower_count = 0
    upper_count = 0
    for s in strs:
        if 'a' <= s <= 'z':
            lower_count += 1
        elif 'A' <= s <= 'Z':
            upper_count += 1
    return [lower_count, upper_count]


if __name__ == '__main__':
    print(capitalization_words("abcABC123,S"))
    print(_capitalization_words("abcABC123,S"))
