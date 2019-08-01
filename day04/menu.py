# coding: UTF-8

"""
=====================水果超市=====================
1.查询全部
2.查询单个
2.增加
3.修改
4.删除
5.离开
=================================================
"""

from fruit import Fruit
from fruit_operate import FruitOperate


class Menu:
    """水果商店"""
    menu_dict = {
        "1": "查询全部",
        "2": "查询单个",
        "3": "增加",
        "4": "修改",
        "5": "删除",
        "6": "离开"
    }

    @staticmethod
    def create_fruit(fruit_info: str):
        """返回一个水果"""
        name, price, amount = fruit_info.split()
        return Fruit(name, float(price), int(amount))

    @staticmethod
    def parse_fruit_info(info_list: list):
        """返回水果的信息(字符形式)"""
        res = ""
        for info in info_list:
            res += (info + "\n")
        return res

    @classmethod
    def parse_success_info(cls, is_success: bool, order: int):
        """返回操作成功与失败的信息"""
        order = str(order)
        if order in ["3", "4", "5"]:
            if is_success:
                return cls.menu_dict[order] + "成功"
            else:

                return cls.menu_dict[order] + "失败" + "，该水果" + str("已在库中" if order == "3" else "不存在")
        else:
            return ""

    def launcher_menu(self):
        """商店入口"""
        oper = FruitOperate([Fruit("苹果", 2, 3), Fruit("香蕉", 1, 5), Fruit("梨子", 6, 6)])   # 用于测试
        while True:
            print("="*21 + "水果超市" + "="*21)
            for menu_order, menu_name in self.menu_dict.items():
                print(menu_order + "." + menu_name)
            print("="*46)
            order = int(input("请输入要操作的序号:"))
            if order == 6:
                break
            elif order == 1:
                info_list = oper.query_all_fruit()
                print(self.parse_fruit_info(info_list))
            elif order == 2:
                info_list = oper.query_single_fruit(input("请输入要查询水果的名字:"))
                print(self.parse_fruit_info(info_list))
            elif order == 3:
                flags = oper.add_fruit(self.create_fruit(input("请输入要添加水果的信息:")))
                print(self.parse_success_info(flags, 3))
            elif order == 4:
                name = input("请输入要修改水果的名字:")
                if oper.judge_fruit_exist(name) is False:
                    print("{}不在库中".format(name))
                    continue
                price = input("请输入要修改水果的价格(回车略过):")
                amount = input("请输入要修改水果的数量(回车略过):")
                flags = oper.modify_fruit(name, price, amount)
                print(self.parse_success_info(flags, 4))
            elif order == 5:
                flags = oper.remove_fruit(input("请输入要删除水果的名字:"))
                print(self.parse_success_info(flags, 5))

        print("="*21 + "再见" + "="*21)


if __name__ == '__main__':
    menu = Menu()
    menu.launcher_menu()


