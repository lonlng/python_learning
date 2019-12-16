# (1)利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']
from functools import reduce

map1 = ['adam', 'LISA', 'barT']


def UpLow(a):
    return a.capitalize()


map2 = list(map(UpLow, map1))
print(map1)
print(map2)


# (2)Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(b):
    return reduce(lambda x, y: x * y, b)


list2 = [1, 5, 7, 9, 4, 6, 4, 6, 7, 4]
sum2 = prod(list2)
print(sum2)

# (3)利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# def str2float(c):
#     return reduce(lambda x,map(int,c))
str = '123145.367'

def map2(d):
    if '.' in d:
        liststr = list(d)[:d.index('.')] + list(d)[d.index('.') + 1:]
        inde = len(d) - d.index('.') - 1
    else:
        liststr = list(d)
        inde = 0
    return reduce(lambda x, y: float(x) * 10 + float(y), liststr) / (10 ** inde)

list55 = map2(str)
print(list55)
