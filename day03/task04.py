# coding: UTF-8
"""
读入 n（>0）名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。

输入格式：
每个测试输入包含 1 个测试用例，格式为

第 1 行：正整数 n
第 2 行：第 1 个学生的姓名 学号 成绩
第 3 行：第 2 个学生的姓名 学号 成绩
  ... ... ...
第 n+1 行：第 n 个学生的姓名 学号 成绩
其中姓名和学号均为不超过 10 个字符的字符串，成绩为 0 到 100 之间的一个整数，这里保证在一组测试用例中没有两个学生的成绩是相同的。

输出格式：
对每个测试用例输出 2 行，第 1 行是成绩最高学生的姓名和学号，第 2 行是成绩最低学生的姓名和学号，字符串间有 1 空格。

输入样例：
3
Joe Math990112 89
Mike CS991301 100
Mary EE990830 95
输出样例：
Mike CS991301
Joe Math990112

"""


class Student:
    """学生成绩类"""
    def __init__(self, name: str, student_id: str, grade: int):
        self.__name = name    # 姓名
        self.__student_id = student_id    # 学号
        self.__grade = grade  # 成绩

    @property
    def name(self):
        return self.__name

    @property
    def student_id(self):
        return self.__student_id

    @property
    def grade(self):
        return self.__grade

    def __str__(self):
        return self.__name + " " + self.__student_id


def main():
    num = int(input("要录成绩的学生数:"))
    student_list = []   # 存放学生对象
    for order in range(num):
        name, student_id, grade = input("第{}个学生:".format(order+1)).split()   # split默认包括空格
        student_list.append(Student(name, student_id, int(grade)))

    return max(student_list, key=lambda stu: stu.grade), min(student_list, key=lambda stu: stu.grade)


if __name__ == '__main__':
    high_stu, low_stu = main()
    print(high_stu)
    print(low_stu)
    # a = Student("Joe", "Math990112", 89)

