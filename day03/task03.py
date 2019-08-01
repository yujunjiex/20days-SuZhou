# coding: UTF-8
""".编写函数，计算形式如a + aa + aaa + aaaa + ... + aaa...aaa的表达式的值，其中a为小于10的自然数。"""


def solve(a: int, n: int):
    """
    计算形式如a + aa + aaa + aaaa + ... + aaa...aaa的表达式的值，其中a为小于10的自然数
    :param a: 小于10的自然数
    :param n: 表达式中的最大值长度
    :return:
        res : 结果
    """
    res = 0
    for x in range(n):
        temp = 0
        for y in range(x+1):
            temp += 10**y * a
        res += temp
    return res


if __name__ == '__main__':
    print(solve(2, 5))
    print(solve(2, 1))
