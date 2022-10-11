#python中的五种数据容器：
#列表list， 元组touple， 字符串str， 集合set， 字典dict

name_list = ["df","dg","as"]
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





