# coding: UTF-8
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def main():
    total = 0
    while True:
        num = input("请输入要加上的数:")
        if is_number(num):
            total += float(num)
        condition = input("要不要继续输入?(yes or no):")
        if condition == "no":
            break

    print("输入数的总和为：", total)


if __name__ == '__main__':
    main()
