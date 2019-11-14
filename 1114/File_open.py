# 1）
print("(1)")
file_01 = open('txt/Test_01.txt', 'r')
content = file_01.readlines()
for i in content:
    if i[0] != '#':
        print(i)
file_01.close()

# 2)
print("(2)")
file_02_r = open('txt/Test_02.txt', 'r')
content_02 = file_02_r.read()
file_02_r.close()
content_002 = content_02.swapcase()
print(content_002)
file_02_w = open('txt/Test_02.txt', 'w')
file_02_w.write(content_002)
file_02_w.close()

# 3)
print("(3)")
file_03_r = open('txt/Test_03.txt', 'r')
content_03 = file_03_r.read()
file_03_r.close()
content_03_list = list(content_03)
content_03_list.sort()
print(content_03_list)

# 4)
print("(4)")
file_04_r = open('txt/Test_04.txt', 'r')
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
        else:
            j = chr(ord(str) + 1)
            del content_04_list[i]
            content_04_list.insert(i, j)
content_04 = ''.join(content_04_list)
print(content_04)
file_04_w = open('txt/Test_04.txt', 'w')
file_04_w.write(content_04)
file_04_w.close()

# 5)
print("(5)")
file_05_r = open('txt/Test_05.txt', 'r', encoding='UTF-8')
content_05 = file_05_r.readlines()
file_05_r.close()
del content_05[2]
content_05 = ''.join(content_05)
print(content_05)
file_05_w = open('txt/Test_05_new.txt', 'w', encoding='UTF-8')
file_05_w.write(content_05)
file_05_w.close()

# 6)
print("(6)")
