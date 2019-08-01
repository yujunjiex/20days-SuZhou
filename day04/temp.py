# coding: UTF-8


def solve(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return solve(n-1) + solve(n-2)


# print(solve(4))

class Car:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, tes):
        print(tes+"come in")


demo = Car(tes="10")


