# coding: UTF-8
"""
猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个，
第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘多少个桃子？
"""


def solve():
    total = 1
    for x in range(1, 10):
        total = (total + 1) * 2
    return total


def _solve(day):
    """递归解法"""
    if day == 10:  # 终止条件：第十天剩一个桃子
        return 1
    return (_solve(day+1) + 1) * 2


if __name__ == '__main__':
    # print(solve())
    print(_solve(1))
