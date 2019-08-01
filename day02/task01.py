# coding: UTF-8
"""编写函数计算圆的面积"""
from math import pi as PI


def calc_circle_area(radius: float):
    """
    计算圆的面积
    :param radius: 圆的半径
    :return: 圆的面积
    """
    return PI*(radius**2)


if __name__ == '__main__':
    print(calc_circle_area(2))
