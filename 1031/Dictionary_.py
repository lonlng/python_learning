import random

print(".1)")
# 赋值 topHitters 字典变量
topHitters = {"Gehrig": {"atBats": 8061, "hits": 2721}, "Ruth": {"atBats": 8399, "hits": 2873},
              "Willams": {"atBats": 7706, "hits": 2654}}

# 创建for循环, 字典topHitters 键被 i 逐个代替,
for i in topHitters:
    print(topHitters[i]['hits'] / topHitters[i]['atBats'])

print('.2)')
# 变量hits -- 总击中球次数, 将字典中元素值逐个相加
hits = 0
for i in topHitters:
    hits += topHitters[i]['hits']
print(hits / 3)

print(".3)max")
G = "Gehrig"
G = "Ruth" if topHitters[G]['hits'] < topHitters['Ruth']['hits'] else "Gehrig"
G = "Willams" if topHitters[G]['hits'] < topHitters['Willams']['hits'] else "Gehrig"
print("击中球次数最多的一位:", topHitters[G]['hits'])

print(".4)")
sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
sinfoList = []
# 将sinfo中的键赋值给sinfoList, 在下一for循环作为序列使用.
for key in sinfo.keys():
    sinfoList.append(key)
for key3 in sinfoList:
    if sinfo[key3] == 1:
        del sinfo[key3]  # 使用删除函数, 删除键
print(sinfo.keys())

print(".5)")
# 将inputString作为输入字符后变量
# inputString = input()
inputString = 'hello java, hello python, hello C.'
print(inputString)
# 使用split函数对inputString 函数进行切片, 默认分割符为空格, 制表, 换行
splitString = inputString.split()
splitStr = []
for i in splitString:
    # 使用 isalpha 函数.判断 i -- 字符串 是否为全为字母
    if not i.isalpha():
        for j in (' .,*'):
            # 再次判断是否全为字母, 主要为了减少for循环次数
            if i.isalpha():
                break
            i = "".join(i.split(j, -1))
    splitStr.append(i)
print("splitStr", splitStr)
# 添加dictNum 变量,先赋值为空,再将单词,及其数量赋值
dictNum = {}
for i in splitStr:
    num = 0
    for j in splitStr:
        if i == j:
            num += 1
    dictNum.update({i: num})
print(dictNum)

print("函数")


def circularArea(r):
    Area = 3.14 * pow(r, 2)
    return Area


print("圆的面积:", circularArea(4))

print("三角形")


def Triangle(a, b, c):
    return (True) if (a + b) > c and (a + c) > b and (b + c) > a else (False)


print("三角形判断", Triangle(33, 39, 30))

print("list 十个整型数")


def listNumber(x, y):
    a = x[y:]
    a = a + x[:y]
    a.reverse()
    return a


aaa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
bbb = listNumber(aaa, 6)
print("listNumber(a,6)=", bbb)

print("抽奖")
a1 = 0
a2 = 0
a3 = 0
for i in range(1000):
    randomA = random.random()
    if randomA > 0 and randomA < 0.08:
        a1 += 1
        continue
    if randomA > 0.08 and randomA < 0.3:
        a2 += 1
        continue
    if randomA > 0.2 and randomA < 1:
        a3 += 1
        continue
ChouJiang = {'一等奖': a1, '二等奖': a2, '三等奖': a3}
print(ChouJiang)
