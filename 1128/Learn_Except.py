'''
1.	编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常
'''


class beijianshubunengxiaouyiyichang(Exception):
    def __init__(self):
        # self.a = a
        # self.b = b
        print("被减数不能小于减数")
try:
    a = 1
    b = 2
    if a < b:
        raise beijianshubunengxiaouyiyichang()
except Exception as e:
    print(e)


# '''
# 2.、定义一个函数func(filename) filename:文件的路径。
# 函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。
# '''

def funcFile(fileName):
    try:
        file_r = open('Test.txt', 'r')
        content = file_r.read()
        file_r.close()
        return content
    except Exception as e:
        print(e)
    else:
        return ("文件打开失败")
    finally:
        return ("heheaa")


funcFile("Test.txt")


# '''
# 3.电脑随机生成1~100随机数，用户输入一个数字，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
# '''
import random
def func03(num1, num2):
    return (True) if num1 < num2 else (False)
number1=random.randint(1,100)
while 1:
    number2 = int(input("请输入整数"))
    if number1==number2 or number2==101:
        print("随机数为",number1)
        break
    if func03(number1,number2):
        print("大")
    else:
        print("小")

# '''
# 4.假设成年人的体重和身高存在此种关系：
# 身高（厘米）-100 = 标准体重（千克）
# 如果一个人的体重与其标准体重的差值在正负5%之间，显示“体重正常”，其他则显示“体重超标”或者“体重不达标”。
# 编写程序，能处理用户输入的异常，并且使用自定义异常类来处理身高小于30cm、大于250cm的异常情况。
# '''
class shengaotizhongguanxi(Exception):
    def __init__(self,num1,num2):
        floatNum1 = (num2-num1)*0.95
        floatNum2=(num2-num1)*1.05
        if num1 > floatNum1:
            print("体重超标")
        elif num1 < floatNum2:
            print("体重不达标")
        else:
            print("体重正常")
number4_1=float(input("体重"))
number4_2=float(input("身高"))

try:
    floatNum1 = (number4_2 - number4_1) * 0.95
    floatNum2 = (number4_2 - number4_1) * 1.05
    if floatNum1 > floatNum1:
        raise shengaotizhongguanxi(number4_1,number4_2)
        # print("体重超标")
    elif floatNum1 < floatNum2:
        raise shengaotizhongguanxi(number4_1, number4_2)
        # print("体重不达标")
    else:
        raise shengaotizhongguanxi(number4_1, number4_2)
        # print("体重正常")
except Exception as e:
    print(e)


# '''
# 5. 自定义一个简易的模块，使这个模块能计算平方根，还能计算加 减 乘。
# '''
def funcArithmetic():

# '''
# 6.编写一个python 程序，从控制台输入两个日期，格式为2011-1-1，然后计算这两个日期之间相差多少天，并输出计算结果。如果输出的时间格式错误，则抛出异常，并输出这个异常。
# Datetime时间模块使用参考：
# https://www.cnblogs.com/fclbky/articles/4098204.html
# '''
