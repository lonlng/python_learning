import random

print(".1)")
topHitters = {"Gehrig": {"atBats": 8061, "hits": 2721}, "Ruth": {"atBats": 8399, "hits": 2873},
              "Willams": {"atBats": 7706, "hits": 2654}}
for i in topHitters:
    print(topHitters[i]['hits'] / topHitters[i]['atBats'])

print('.2)')
hits = 0
for i in topHitters:
    hits += topHitters[i]['hits']
print(hits / 3)

print(".3)max")
G = "Gehrig"
GehriGhits = topHitters['Willams']['hits']
G = "Ruth" if topHitters[G]['hits'] < topHitters['Ruth']['hits'] else "Gehrig"
G = "Willams" if topHitters[G]['hits'] < topHitters['Willams']['hits'] else "Gehrig"
print("击中球次数最多的一位:", topHitters[G]['hits'])

print(".4)")
sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
print(sinfo.keys())
sinfoList = []
for key4 in sinfo.keys():
    sinfoList.append(key4)
for key3 in sinfoList:
    print(key3)
    print(sinfo[key3], "\n", type(sinfo[key3]))
    if sinfo[key3] == 1:
        del sinfo[key3]
print(sinfo.keys())

print(".5)")

inputString = 'hello java, hello python, hello C.'

splitString = inputString.split()
print(splitString)
print(type(splitString))

splitString_3 = []
print(type(splitString_3))
for i in splitString:
    splitString_2 = i
    if not i.isalpha():
        for j in (' .,*'):
            if i.isalpha():
                break
            splitString_2 = "".join(i.split(j, -1))
            i = splitString_2
    splitString_3.append(splitString_2)
print("splitString_3", splitString_3)
num = 0
num2 = {}
for i in splitString_3:
    num = 0
    for j in splitString_3:
        if i == j:
            num += 1
    num3 = {i: num}
    num2.update(num3)
print(num2)

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
