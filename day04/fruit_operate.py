# coding: UTF-8


class FruitOperate:
    """对水果集合的操作"""
    def __init__(self, fruit_list=None):
        if fruit_list is not None:
            self.fruit_dict = self.__get_fruit_dict(fruit_list)
        else:
            self.fruit_dict = {}    # 存放水果信息的列表

    @staticmethod
    def __get_fruit_dict(fruit_list):
        """把传进来的水果信息转换成字典格式"""
        fruit_dict = {}
        for fruit in fruit_list:
            fruit_dict[fruit.name] = fruit
        return fruit_dict

    def judge_fruit_exist(self, name):
        """判断水果在不在库中"""
        if name in self.fruit_dict:
            return True
        else:
            return False

    def query_all_fruit(self):
        """查询全部"""
        info_list = ["共查询到{}条记录".format(len(self.fruit_dict))]
        for fruit in self.fruit_dict.values():
            info_list.append(fruit.name + " 价格:" + str(fruit.price) + "  数量:" + str(fruit.amount))
        return info_list

    def query_single_fruit(self, fruit_name: str):
        """根据水果名查询水果信息"""
        info_list = []
        if fruit_name in self.fruit_dict:
            fruit = self.fruit_dict[fruit_name]
            info_list.append(fruit.name + " 价格:" + str(fruit.price) + "  数量:" + str(fruit.amount))
        else:
            info_list.append("库存中没有{}".format(fruit_name))
        return info_list

    def add_fruit(self, fruit):
        """增加一种水果"""
        if fruit.name in self.fruit_dict:
            return False
        self.fruit_dict[fruit.name] = fruit
        return True

    def modify_fruit(self, name: str, price=None, amount=None):
        """修改水果信息"""
        if name in self.fruit_dict:
            if price is not None and price != "":
                self.fruit_dict[name].price = price
            if amount is not None and amount != "":
                self.fruit_dict[name].amount = amount
            return True
        else:
            return False

    def remove_fruit(self, name):
        """删除指定名字的水果"""
        if name in self.fruit_dict:
            self.fruit_dict.pop(name)
            return True
        else:
            return False
