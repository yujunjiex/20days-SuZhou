# coding: UTF-8
"""编写函数，接收包含20个整数的列表lst和一个整数k作为参数，返回新列表。
处理规则为：将列表lst中下标k之前的元素逆序，下标k之后的元素逆序，然后将整个列表lst中的所有元素再逆序。"""


def reverse_list(k: int):
    lyst = list(range(8))
    assert 0 < k < len(lyst)-1
    return lyst[k+1:] + [lyst[k]] + list(reversed(lyst[:k]))  # k之后的list+lyst[k]+k之前的list逆序


print(reverse_list(4))

