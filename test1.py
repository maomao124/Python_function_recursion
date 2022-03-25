"""
 * Project name(项目名称)：Python函数递归
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 21:38
 * Version(版本): 1.0
 * Description(描述)： 
 """


def f1(num):
    """
    累加
    :param num:
    :return:
    """
    if num > 0:
        return num + f1(num - 1)
    else:
        return 0


def f2(num):
    """
    累乘
    :param num:
    :return:
    """
    if num > 0:
        return num * f2(num - 1)
    else:
        return 1


def f3(num):
    """
    累乘,栈溢出
    :param num:
    :return:
    """
    return num * f3(num - 1)


if __name__ == '__main__':
    print(f1(3))
    print(f1(4))
    print(f1(5))
    print(f1(6))
    print(f1(7))
    print(f1(8))
    print(f1(9))
    print(f1(10))

    print(f2(3))
    print(f2(4))
    print(f2(5))
    print(f2(6))
    print(f2(7))
    print(f2(8))
    print(f2(9))
    print(f2(10))

    # print(f3(5))
