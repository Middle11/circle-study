"""i = 0
while i <= 3:
    i += 1
    print("huhu")

sum = 0
x = 1
while x < 101:
    sum = sum + x
    x += 1
print(sum)   #输出5050

sum = 0
x = 1
while x < 101:
    sum = sum + x
    x += 1
print("sum")   #输出sum

import random
num = random.randint(1,100)
speculation = int(input("输入猜测的数字："))

while speculation != num:

    if speculation > num:
            print("猜大啦")
            speculation = int(input("输入猜测的数字：")) #while循环需要一个出口，这行就是出口
    else:
            print("猜小啦")
            speculation = int(input("输入猜测的数字："))
print("恭喜恭喜对了")
print("游戏结束")

name = "sxclzt"
for s in name:
    print(s)

for x in range(5,10,2):
    print(x)



i = 1
while i <= 5:
    print(f"今天是学习的第{i}天")
    for j in range(1, 4):
        print(f"今天学习的第{j}节")
    i += 1
print(f"今天是学习的第{i-1}天,学习完成")

i = 1
while i <= 5:
    print(f"今天是学习的第{i}天")
    j = 1
    while j <= 3:
        print(f"今天学习的第{j}节")
        j += 1
    i += 1
print(f"今天是学习的第{i-1}天,学习完成")"""

#for循环的嵌套
#案例：学习python十天，每天学三节
i = 1
x = 1

for i in range(1,6):
    print(f"今天是学习的第{i}天")
    for j in range(x, x + 3):

        print(f"今天学习的第{j}节")
        x += 1
print(f"今天是学习的第{i}天,学习完成")

