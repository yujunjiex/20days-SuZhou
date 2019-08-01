# coding: UTF-8
"""输出小于100的最大素数"""
# Todo:素数——除了1和它本身以外不再有其他因数 ，且是大于1的自然数


def get_max_prime_num(low: int, high: int):
    """
    获取范围low~high之间的最大素数
    :param low: 范围最小值
    :param high: 范围最大值
    :return: max_num:int 最大素数
    """
    assert low < high
    assert low > 1
    for value in range(high, low-1, -1):
        prime = True
        for i in range(low, value):  # 判断在value之前的数能否把value整除
            if value % i == 0:
                prime = False
                break
        if prime is True:
            return value


if __name__ == '__main__':
    # func01
    print(get_max_prime_num(2, 100))
    # func02
    print(max(["%s" % x for x in range(2, 100) if not [y for y in range(2, x) if x % y == 0]]))

