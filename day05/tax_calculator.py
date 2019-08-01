# coding: UTF-8
"""
实现一个个税计算器，可以计算并打印税后工资。(用函数实现)

项目需求：
输入税前工资
输出税后工资
计算过程需要扣除社会保险费用


个税计算公式：

应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
其中各项社会保险费我们在本程序中需要计算，计算公式由于各地不一样，我们此处使用国内某一城市的计算比例，占工资金额的比例如下：

养老保险：8%
医疗保险：2%
失业保险：0.5%
工伤保险：0%
生育保险：0%
公积金：6%
注意，此处不考虑社保缴费基数的问题。直接使用工资金额计算社保费用即可。

税率及速算扣除数对应表：

全月应纳税额  税率  速算扣除数（元）
不超过 1500 元 3% 0
超过 1500 元至 4500 元 10% 105
超过 4500 元至 9000 元 20% 555
超过 9000 元至 35000 元 25% 1005
超过 35000 元至 55000 元 30% 2755
超过 55000 元至 80000 元 35% 5505
超过 80000 元 45% 13505
例如工资金额为 5000，那么五险一金缴纳 825 元，应纳税所得额为 675（5000-825-3500），
应纳税额为 20.25 元（675*%3 - 0）。税后工资为 4154.75（5000-825-20.25）。
"""

"""
五险一金 16.5%
"""


def solve(pay: float):
    起征点 = 3500
    if pay <= 起征点:
        return pay

    工资金额 = pay
    应纳税额 = 0
    tax_dict = {1500: 0.03, 4500: 0.1, 9000: 0.2, 35000: 0.25, 55000: 0.3, 80000: 0.35, float("inf"): 0.45}
    deduction_dict = {1500: 0, 4500: 105, 9000: 555, 35000: 1005, 55000: 2755, 80000: 5505, float("inf"): 13505}
    五险一金 = 工资金额*0.165
    应纳税所得额 = 工资金额 - 五险一金 - 起征点
    if 应纳税所得额 <= 0:
        return 工资金额
    for tax in tax_dict.keys():
        if tax >= 应纳税所得额:
            应纳税额 = 应纳税所得额 * tax_dict[tax] - deduction_dict[tax]
            break

    return 工资金额 - 五险一金 - 应纳税额   # 税后工资


print(solve(3800))
print(solve(4500))
print(solve(5000))
print(solve(50000))

