# coding: UTF-8
"""计算 1+2+3+...+100"""


if __name__ == '__main__':
    # func01
    total = 0
    for value in range(1, 101):
        total += value

    print(total)

    # func02
    print(sum([value for value in range(1, 101)]))
