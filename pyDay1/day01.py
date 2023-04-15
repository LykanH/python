# salary = 123;
# name = "zhangsan"
# print(name)
#
# s = input("请输入：")   #字符串
# print(s)

#列表
#存储
# list = []
# list0 = ["sss",True,1,2.0]
# print(list0)
#
# #添加
# list0.append("hello")
# print(list0)
#
# list0.insert(2,"123")
# print(list0)
# print(len(list0))

# a和b值一样   地址值相同
# a和b值不一 样 地址值不同
# a = 10
# b = 10
# print(id(a))
# print(id(b))


# 银行取钱
# balence = 326
# drawMoney = int(input("输入取钱金额:"))
# # print(balence)
#
# if drawMoney<balence and drawMoney%100!=0 :
#     print("不支持！")
# elif(balence<drawMoney):
#     print("余额不足！")
# else:
#     balence-=drawMoney
#     print("余额为:%d"%balence)

import math
l1 = []

for i in range (1,101):
    f = True
    # if(i<2): f = True
    for j in range (2,int(math.sqrt(i))+1):
        if(i%j==0): f = False

    if(f):l1.append(i)
    # for j in range(2,i/j+1) :
print(l1)


# 字符串