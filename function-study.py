#python中的五种数据容器：


#列表list， 元组touple， 字符串str， 集合set， 字典dict

"""name_list = ["df","dg","as"]
name_list[0] = 1 #修改元素
name_list.insert(2,"dfgh") #插入元素
name_list.append([6,7,8]) #在列表尾部追加元素
print(name_list)
print(type(name_list))

print(name_list[0])
print(name_list[1])
print(name_list[2])

print(name_list.index("dg"))

list_test = [[1,2,3],["df","dg","as"]]
print(list_test)
print(type(list_test))

print(list_test[0])
print(list_test[1])

print(list_test[0][0])
print(list_test[0][1])
print(list_test[0][2])

print(list_test[1][0])
print(list_test[1][1])
print(list_test[1][2])

anyway_list1 = ["df","dg","as"]
anyway_list1.extend([1]) #在列表尾部追加元素
print(anyway_list1)

anyway_list2 = ["df","dg","as"]
del anyway_list2[1] #删除元素（下标）
print(anyway_list2)

anyway_list3 = ["df","dg","as"]
anyway_list3.pop(1) #删除元素（下标）
print(anyway_list3)

anyway_list4 = ["df","dg","as","df"]
anyway_list4.remove("df") #删除第一个匹配到的元素（元素）
print(anyway_list4)

anyway_list5 = ["df","dg","as","df"]
anyway_list5.clear() #清空列表内容
print(anyway_list5)

anyway_list6 = ["df","dg","as","df"]
print(anyway_list6.count("df")) #统计某元素在列表内的数量

anyway_list8 = ["df","dg","as","df"]
print(len(anyway_list8))

#列表的遍历
index = 0
while index < len(anyway_list8):
    x = anyway_list8 [index]
    index += 1
    print(x)
for i in anyway_list8:
    print(i)

#元组touple
t1 = (1,"hey",True)
t2 = ("hey",) #元组内只有一个数据时，数据后面也要加逗号
print(t1,t2)
t3 = ((1,"hey",True),(1,2,3))
print(t3)
t4 = (1,2,"hey",2,3,4,"hey")
print(t4[2])
print(t4.index(2))
print(t4.count("hey"))
print(t4.count(2))
print(len(t4))

#字符串
str1 = "ituj and ti itfgh"
print(str1.count("it")) #count用于统计字符串中某字符出现的次数，其中it是作为一个整体统计

str2 = "12fgdfh and fdyfdy21"
print(str2.strip("12")) #字符串的规整操作，字符串.strip（字符串）是去前后指定字符串，传入的是“12”，其实就是1和2都会被移除，是按照单个字符

str3 = " ituj and ti itfgh "
print(str3.strip()) #字符串的规整操作，字符串.strip（）是去前后空格
print(len(str3)) #空格，数字，符号，中文，字母算在字符串的长度里面

#集合set
#集合不支持元素的重复，并且内容无序

set1 = {"hj","123","dgfh","hj","fd3"}
print(set1)

set2 = {"hj","123"}
set2.add("dfgh") #添加指定元素
print(set2)

set3 = {"hj","123","dgfh","hj","fd3"}
set3.remove("123") #移除指定元素
print(set3)

set4 = {"hj","123"}
element = set4.pop() #随机取出一个元素
print(set4)
print(element)

set5 = {"hj","123"}
set5.clear()
print(set5)

set6 = {1,2,3}
set7 = {1,5,6}
set8 = set6.difference(set7) #集合1.difference（集合2），取出集合1有而集合2没有的元素，得到一个新集合，集合1和集合2不变
print(set6,set7,set8)

set9 = {1,2,3}
set10 = {1,5,6}
set9.difference_update(set10) #集合1.difference_uodate（集合2）,删除集合1内和集合2相同的元素，
print(set9,set10)

set11 = {1,2,3}
set12 = {1,5,6}
set13 = set11.union(set12) #组成新集合
print(set11,set12,set13)
print(len(set11))

for i in set11:
    print(i)


#dict
score1 = {"asd":89,"fgh":90,"jkl":99}
print(score1["asd"])
print(score1["fgh"])
print(score1["jkl"])

score2 = {"asd":{"语文":78,"数学":79,"英语":90},
          "fgh":{"语文":78,"数学":79,"英语":90},
          "jkl":{"语文":78,"数学":79,"英语":90}}
print(score2["asd"])
print(score2["asd"]["数学"])

score3 = {"asd":89,"fgh":90,"jkl":99}
score3["qwe"] = 78 #新增元素
print(score3)

score4 = {"asd":89,"fgh":90,"jkl":99}
score4["asd"] = 99 #更新元素
print(score4)

score5 = {"asd":89,"fgh":90,"jkl":99}
value = score5.pop("asd") #删除元素
print(value)
print(score5)
score5.clear() #清空字典
print(score5)

score6 = {"asd":89,"fgh":90,"jkl":99}
print(len(score6)) #计算键值对的数量
keys = score6.keys() #获取全部的key
print(keys)
for i in keys: #遍历字典
    print(f"学生：{i},分数：{score6[i]}")"""


#函数

def add(x,y):
    result = x + y
    print(f"{x}+{y}的结果是{result}")
add(5,6)

def add(a,b):
    result = a + b
    return result
r = add(1,2)
print(r)


