# 1）
print("(1)")
file_01 = open('Test_01.txt', 'r')
content = file_01.readlines()
for i in content:
    # print('i=',i)
    if i[0] != '#':
        print(i)
file_01.close()

# 2)
print("(2)")
file_02_r = open('Test_02.txt', 'r')
content_02 = file_02_r.read()
file_02_r.close()
content_002 = content_02.swapcase()
print(content_002)
file_02_w = open('Test_02.txt', 'w')
file_02_w.write(content_002)
file_02_w.close()

# 3)
print("(3)")
file_03_r = open('Test_03.txt', 'r')
content_03 = file_03_r.read()
file_03_r.close()
content_03_list = list(content_03)
content_03_list.sort()
print(content_03_list)

# 4)
print("(4)")
file_04_r = open('Test_04.txt', 'r')
content_04 = file_04_r.read()
file_04_r.close()
content_04_list = list(content_04)
for i in range(len(content_04_list)):
    str = content_04_list[i]
    if str.isalpha():
        if ord(str) == 90 or ord(str) == 122:
            j = chr(ord(str) - 25)
            del content_04_list[i]
            content_04_list.insert(i, j)
            content_04_list.insert(i, j)
        else:
            j = chr(ord(str) + 1)
            del content_04_list[i]
            content_04_list.insert(i, j)
print(content_04_list)
# file_04_w = open('Test_04.txt', 'w')
# file_04_r.close()
