# coding: UTF-8
"""
编写函数模拟猜数游戏。系统随机产生一个数，玩家最多可以猜5次，
系统会根据玩家的猜测进行提示，玩家则可以根据系统的提示对下一次的猜测进行适当调整。
"""
import random


class GuessNumberGame:
    """一个简单的猜数游戏"""
    def __init__(self, low=0, high=100, guess_times=5):
        assert low < high
        self.low = low  # 猜测范围
        self.high = high
        self.guess_times = guess_times  # 猜测次数

        self.answer = None  # 正确答案

    @staticmethod
    def __tip(answer: int, num: int):
        """
        用于提示的工具函数
        :param answer:正确答案
        :param num: 用户猜测的数
        :return:
            0 表示num<answer 猜小了
            1 表示num>answer 猜大了
            2 num==answer猜测正确
        """
        if num == answer:
            return 2
        return 0 if num < answer else 1

    def game_launcher(self):
        """游戏流程"""
        print("*" * 10 + "欢迎来到猜数字游戏" + "*" * 10)
        print("游戏说明: 系统会随机生成{}-{}的整数，"
              "您有{}次猜测机会(按下回车键开始...)".format(self.low, self.high, self.guess_times), end="")
        input()
        while True:
            print("*" * 10 + "游戏开始" + "*" * 10)
            self.answer = random.randint(self.low, self.high)
            for x in range(1, self.guess_times+1):
                if x == self.guess_times:
                    print("最后一次机会了，加油！", end="")
                guess_num = int(input("输入你第{}次猜测的数:".format(x)))    # 这里懒得做输入检测了

                flag = self.__tip(self.answer, guess_num)
                if flag == 2:
                    print("猜中了!正确数字是{}".format(self.answer))
                    break
                elif x == self.guess_times:  # 最后一次猜测失败的情况
                    print("猜错了，你的机会用完了，正确答案是{}".format(self.answer))

                elif flag == 0:
                    print("猜小了 再试试")
                elif flag == 1:
                    print("猜大了 再试试")
            chioce = input("继续下一把游戏吗？(yes or no)").lower()
            if chioce == "no":
                break
        print("*"*10+"再见"+"*"*10)


if __name__ == '__main__':
    demo = GuessNumberGame()
    demo.game_launcher()
