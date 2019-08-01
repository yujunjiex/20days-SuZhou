# coding: UTF-8
""" 编写函数，接收整数参数t，返回斐波那契数列中大于t的第一个数。"""


def _fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return _fibonacci(n-1)+_fibonacci(n-2)


def decorate_fib(t):
    n = 1
    while True:
        res = _fibonacci(n)
        n += 1
        if res > t:
            return res


def fibonacci(t):
    pre_fib = 1
    current_fib = 1  # 直接从第二个开始
    while True:
        if current_fib > t:
            return current_fib
        else:
            current_fib, pre_fib = pre_fib+current_fib, current_fib


if __name__ == '__main__':
    print(fibonacci(0))

    print(decorate_fib(3))

