# coding: UTF-8
"""
系统，把水果上架，水果有价格，要能看到，然后看到所有的水果
水果价格按照从小到大，下架，能查到任何一笔水果的信息。

=====================水果超市=====================
1.查询全部
2.增加
3.修改
4.删除
...
=================================================

选择1：查询全部
选择2：增加功能

"""


class Fruit:
    """水果信息类"""
    def __init__(self, name: str, price: float, amount: int):
        self.__name = name  # 水果名
        self.__price = price    # 价格
        self.__amount = amount  # 数量

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount





