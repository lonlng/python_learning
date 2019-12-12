'''
一、定义一个学生Student类。有下面的属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
方法：
1 获取学生的姓名：get_name()
2 获取学生的年龄：get_age()
3 返回3门科目中最高的分数。get_course() 返回类型:int
class Student:
	def __init__(self,……):

	def get_name(self):
		return self.name

	def get_course(self):
		return max(self.score)

写好类以后，可以定义2个同学测试下:
zm = Student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100
'''


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getScore(self):
        return max(self.score)


s = Student('小明', 19, [70, 100, 90])
print(s.getName(), s.getAge(), s.getScore())


# 二、定义一个字典类：dictclass。完成下面的功能：
# dict1 = {‘key’:value}
# del dict1[‘key’]
# __init__(self,你需要操作的字典):
# 	self.dict1 = 你需要操作的字典
# dict = dictclass({你需要操作的字典})
# 1 删除某个key
# del_dict(self,key)
# 	del self.dict1[key]
#
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(self,key)
# if	key in self.dict1.keys():
#
# else:
# 3 返回键组成的列表：返回类型;(list)
# get_key()

class dictclass:
    def __init__(self, dict):
        self.dict1 = dict

    def del_dict(self, key):
        del self.dict1[key]

    def get_dict(self, key):
        if key in self.dict1.keys():
            return self.dict1[key]
        else:
            return 'not found'

    def get_key(self, key):
        return self.dict1.keys()


s2 = dictclass(({'key1': 10, 'key2': 133}))
print(s2.get_dict('kee'))


# 三、定义一个列表的操作类：Listinfo
# 包括的方法:
# 1
# 列表元素添加: add_key(keyname)[keyname:字符串或者整数类型]
# 2
# 列表元素取值：get_key(num)[num:整数类型]
# 3
# 列表合并：update_list(list)[list:列表类型]
# 4
# 删除并且返回最后一个元素：del_key()
# a = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])

class ListInfo:
    def __init__(self, list):
        self.list = list

    def add_dict(self, keyName):
        self.list.append(keyName)
        return self.list

    def get_key(self, num):
        return self.list[num]

    def update_list(self, list1):
        self.list.extend(list1)
        return self.list

    def del_key(self):
        temp = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]
        return temp


s2 = ListInfo([1, 2, 3, 5, 7, 8, 9, 4, 6, 4, 6, 5])
s2.update_list([99, 88, 77])

print(s2.update_list([99, 88, 77]))
print(s2.del_key())
print(s2.add_dict(13))
