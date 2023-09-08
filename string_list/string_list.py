#f的使用 （要在字符串中插入变量，可在左引号中插入f,变量放在花括号中）
# name_fist="无"
# name_last="痕"
# name=f"你好，{name_fist}{name_last}\n" #f,将变量连接到字符串中
# print(name)

#删除空白 (lstrip()左,rstrip()右,strip()左右)  strip-去除
#删除空白是临时的，要永久生效要将结果重新赋值到变量
# name=" 刘 "
# print(name.lstrip())#左空白删除了
# print(name)#左空白出现，要永久删除  name=name.lstrip()
# name=name.lstrip()
# print(name)

#删除前缀 removeprefix(string)  删除后缀removesuffix(string)
#同删除空白相同，删除是临时的，要永久删除重新赋值变量
# urc="https:www.baidu.com"
# print(urc)
# urc=urc.removeprefix("https:")
# print(urc)

#首字母大写 title() 字母大写 upper()  字母小写 lower()
#同删除空白相同，删除是临时的，要永久删除重新赋值变量
# name_fist="liu"
# name_last="jun"
# print(name_fist.title())
# name_fist=name_fist.title()
# print(name_fist)

#创建的列表是动态的，索引为-1可查找到列表最后一个元素，-2倒数第二个，以此类推
#name=[]  #空列表，后面可追加元素
# name=["刘","李","张"]
# print(name)
# print(name[-1])

#在列表末尾追加元素 append(元素)  插入元素 insert(索引，元素) 要有插入的位置索引和元素
# name=["刘",'李']
# name.append('张')
# print(name) 
# name.insert(0,'万')
# print(name)

#删除列表任意位置元素 del
# name=["刘","李","张"]
# del name[0]
# print(name)



