# coding: UTF-8

# a = list(map(int, "456789"))    # 迭代器 python里一切都是迭代器，序列 这些类中实现的一个方法__iter__
# print(a)
#
# b = list(zip(a, [1, 2, 3]))
# print(b)
#
#
# _, *_, a = 1, 2, 3, 4, 5
# print(a)

temp_dict = {}


def count(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in temp_dict.keys():   # 做个缓存
        return temp_dict[n]

    temp_num = count(n - 1) + count(n - 2)
    temp_dict[n] = temp_num
    return temp_num


# print(count(5))
data = list(range(10))

import random
random.shuffle(data)    # 打乱list
# print(data)


# 对字符串的操作
strs = "123456789"


# 性质判定
print(isinstance(strs, str))
print(type(strs) is str)
print(strs.isalnum())   # 字符串中的所有字符是否都是字母数字且至少有一个字符
print(strs.isalpha())   # 字符串中的所有字符是否都是字母
print(strs.isdigit())   # 字符串中的所有字符是否都是数字
print(strs.isdecimal()) # 字符串中是否只有十进制数

print(strs.islower())   # 字符串中是否都是小写字符且至少有一个字符
print(strs.startswith("123"))    # 检查字符串是否是以指定子字符串开头
print(strs.endswith("789"))     # 检查字符串是否是以指定子字符串结尾

# 查找和替换
print(strs.count("5"))
print(strs.find("5"))   # 找不到会返回-1
print(strs.index("5"))  # 找不到会抛出ValueError异常

print(strs.replace("5", "6"))
print(strs.replace("6", "5", 0))   # 只替换一次(默认全部替换)

# 切片和连接
print(strs.partition("5"))
print(strs.split("5"))
print(strs[1:])
print(strs[:-1])
print(strs[::-1])

# 变形
print("hellO woRld".title())
print("hellO woRld".capitalize())
print("hellO woRld".swapcase())
import string
print("    hellO   woRld ".title())
print("    hellO   woRld ".strip())
print(string.capwords("    hellO   woRld "))


# 对齐
print("hellO woRld".title().center(100, "*"))
print("hellO woRld".title().ljust(100, "*"))
print("hellO woRld".title().rjust(100, "*"))
print("hellO woRld".title().zfill(100))    # z指的是zero,故用0填充，常用于输出数值






