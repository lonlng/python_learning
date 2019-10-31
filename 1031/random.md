### 描述
random() 方法返回随机生成的一个实数，它在[0,1)范围内。

---

### 语法
以下是 random() 方法的语法:

---

* import random     #导入包
* random.random()   #使用函数

**注意：random()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法.**

---

### 返回值

返回随机生成的一个实数，它在[0,1)范围内。

---

### 实例
以下展示了使用 random() 方法的实例：

 ~~~
import random
 
* 生成第一个随机数
print "random() : ", random.random()
 
* 生成第二个随机数
print "random() : ", random.random()
~~~
以上实例运行后输出结果为：

~~~
random() :  0.281954791393
random() :  0.309090465205
~~~
### 实例一
~~~
print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
~~~

---

### 实例二
~~~

import random
import string

# 随机整数：
print random.randint(1,50)

# 随机选取0到100间的偶数：
print random.randrange(0, 101, 2)

# 随机浮点数：
print random.random()
print random.uniform(1, 10)

# 随机字符：
print random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')

# 多个字符中生成指定数量的随机字符：
print random.sample('zyxwvutsrqponmlkjihgfedcba',5)

# 从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print ran_str

# 多个字符中选取指定数量的字符组成新字符串：
print ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))

# 随机选取字符串：
print random.choice(['剪刀', '石头', '布'])

# 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print random.shuffle(items)

~~~