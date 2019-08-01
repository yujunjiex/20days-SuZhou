# coding: UTF-8
"""鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只"""
# TODO:鸡+兔 = 30 ，2*鸡 + 4*兔 = 90

if __name__ == '__main__':
    rabbit = (90 - 60)//2
    chicken = 30 - rabbit

    print("鸡{}只，兔{}只".format(chicken, rabbit))
