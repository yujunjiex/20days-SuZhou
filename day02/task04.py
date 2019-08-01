# coding: UTF-8
"""
让我们用字母 B 来表示“百”、字母 S 表示“十”，用 12...n 来表示不为零的个位数字 n（<10），换个格式来输出任一个不超过 3 位的正整数。
例如 234 应该被输出为 BBSSS1234，因为它有 2 个“百”、3 个“十”、以及个位的 4。

输入格式：
每个测试输入包含 1 个测试用例，给出正整数 n（<1000）。

输出格式：
每个测试用例的输出占一行，用规定的格式输出 n。

输入样例 1：
234
输出样例 1：
BBSSS1234
输入样例 2：
23
"""


def report_num(num):
    """报数"""
    lyst_num = [0, 0, 0]   # 存放"百十个"位
    for x in range(2, -1, -1):
        lyst_num[2-x] = num // 10 ** x % 10
    return lyst_num[0]*"B" + lyst_num[1]*"S" + "".join(map(str, range(0, lyst_num[2]+1)))[1:]  # 删去第一个字符


if __name__ == '__main__':
    print(report_num(23))
    print(report_num(0))

