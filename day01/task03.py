# coding: UTF-8
"""输出水仙花数（要求使用map）"""


def is_daffodil_number(num: int):
    """判断一个数是否为水仙花数"""
    a, b, c = map(int, str(num))
    if a ** 3 + b ** 3 + c ** 3 == num:
        return True


if __name__ == '__main__':
    lyst = []
    for value in range(100, 1000):
        if is_daffodil_number(value):
            lyst.append(value)

    print(lyst)
