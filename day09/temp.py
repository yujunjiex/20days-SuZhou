# coding: UTF-8
# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print(type(matchObj))
#     print(type(matchObj.group()))
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

import numpy as np

data1 = [6, 7.5, 8, 9, 0]
arr1 = np.array(data1)
print(arr1)


data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)    # 数组维度
print(arr2.shape)

print(np.empty((2, 3, 2)))  # 返回的都是随机值
print(np.empty((3, 2)))

arr = np.arange(10)
arr[5:8] = 10   # 广播
print(arr)

arr_slice = arr[5:8]    # 如果要的是切片的副本而不是视图，则应该用arr[5:8].copy()
arr_slice[1] = 12345
print(arr)

