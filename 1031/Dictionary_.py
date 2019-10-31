topHitters = {"Gehrig": {"atBats": 8061, "hits": 2721}, "Ruth": {"atBats": 8399, "hits": 2873},
              "Willams": {"atBats": 7706, "hits": 2654}}
print(topHitters['Gehrig']['hits'] / topHitters['Gehrig']['atBats'])
print(topHitters['Ruth']['hits'] / topHitters['Ruth']['atBats'])
print(topHitters['Willams']['hits'] / topHitters['Willams']['atBats'])

print((topHitters['Gehrig']['hits'] + topHitters['Ruth']['hits'] + topHitters['Willams']['hits']) / 3)
print("max")
if topHitters['Gehrig']['hits'] > topHitters['Ruth']['hits'] and topHitters['Ruth']['hits'] > topHitters['Willams'][
    'hits']:
    print(topHitters['Gehrig']['hits'])
elif topHitters['Ruth']['hits'] > topHitters['Gehrig']['hits'] and topHitters['Ruth']['hits'] > topHitters['Willams'][
    'hits']:
    print(topHitters['Ruth']['hits'])
else:
    print(topHitters['Willams']['hits'])

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
print("splitString_3",splitString_3)
num=0
num2 ={}
for i in splitString_3:
    num=0
    for j in splitString_3:
        if i == j :
            num+=1
    num3={i:num}
    num2.update(num3)
print(num2)
# ifStr=''
# for i in range(len(splitString)):
#     if not splitString[i].isalpha():
#         print(splitString[i])
#         for splitWord in splitString[1]:
#             if (65<=ord(splitWord) and 90>= ord(splitWord)) or (97<=ord(splitWord) and 122>= ord(splitWord)):
#                 ifStr=ifStr+splitWord
#         splitString[i]=ifStr
#     ifStr=''
print("函数")
def circularArea(r):
    Area = 3.14 * pow(r,2)
    return Area
print("圆的面积",circularArea(4))

