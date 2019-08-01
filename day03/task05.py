# coding: UTF-8
"""
给定数字 0-9 各若干个。你可以以任意顺序排列这些数字，但必须全部使用。目标是使得最后得到的数尽可能小（注意 0 不能做首位）。
例如：给定两个 0，两个 1，三个 5，一个 8，我们得到的最小的数就是 10015558。

现给定数字，请编写程序输出能够组成的最小的数。

输入格式：
输入在一行中给出 10 个非负整数，顺序表示我们拥有数字 0、数字 1、……数字 9 的个数。整数间用一个空格分隔。
10 个数字的总个数不超过 50，且至少拥有 1 个非 0 的数字。

输出格式：
在一行中输出能够组成的最小的数。

输入样例：
2 2 0 0 0 3 0 0 1 0
输出样例：
10015558

"""


def solve(lyst: list):
    num_list = lyst.copy()   # 存放拥有对应数字的个数
    num_count = sum(num_list)    # 10个数字的总个数

    flags = False  # 是否拥有1个非0的数字
    res = ""    # 结果
    for num in num_list[1:]:
        if num != 0:
            flags = True
            break

    assert flags is True
    assert num_count < 50

    for order in range(num_count):
        if order == 0:  # 第一个数字要分开处理
            for inner_order, num in enumerate(num_list[1:]):
                if num != 0:
                    res += str(inner_order+1)
                    num_list[inner_order+1] -= 1
                    break
        else:
            for inner_order, num in enumerate(num_list):
                if num != 0:
                    res += str(inner_order)
                    num_list[inner_order] -= 1
                    break

    return res


if __name__ == '__main__':
    # print(solve([2, 2, 0, 0, 0, 3, 0, 0, 1, 0]))
    print(solve([3,2,2,1,4,1,3]))



