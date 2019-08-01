# coding: UTF-8
def split_num(num: int):
    """整除7，不能整除5"""
    if num % 7 == 0 and num % 5 != 0:
        return True


for i in range(1, 101):
    if split_num(i):
        print(i)


# 乘法口诀表
for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}*{1}={2}".format(i, j, i*j), end=" ")
    print("")
