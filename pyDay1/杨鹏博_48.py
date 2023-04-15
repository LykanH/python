# 1.银行取钱

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


# 2.判断质数


# import math
# l1 = []
#
# for i in range (1,101):
#     f = True
#     # if(i<2): f = True
#     for j in range (2,int(math.sqrt(i))+1):
#         if(i%j==0): f = False
#
#     if(f):l1.append(i)
#     # for j in range(2,i/j+1) :
# print(l1)


# 3.字符串
 #1.+ 字符串连接
s1 = "welcome"
s2 = " to China"
print(s1 + s2)
s3 = "good"
print(s3 * 3)
s4 = "abcdef"
print(s4[1])
for element in s4:
    print(element)
for index in range(0,len(s4)):
    print(s4[index])
for index,str in enumerate(s4):
    print(index,str)
str1 = "hello world"
print(str1[3:7])
print(str1[3:])
print(str1[:7])

str2 = "abc123456"
print(str2[2:5]) #c12
print(str2[2:]) #c123456
print(str2[2::2]) #c246
print(str2[::2]) #ac246
print(str2[::-1]) #654321cba 倒序
print(str2[-3:-1]) #45 -1表示最后一个字符
str3 = "today is a good day"
print("good" in str3)
print("good1" not in str3)

#1.计算字符串长度 len
str1 = "hfufhja"
l = len(str1)
print(l)
str2 = "this is a good day good day"
print(str2.count("day"))
print(str2.count("day",3,10))

#8.分割和合并
str3 = "today is a good day"
print(str3.split(" "))
print(str3.split(" ",2))
str4 = "today"
print(str4.splitlines(True)) 



# 单张图片

# 爬虫分析
# 1.找到你的网址，打开网址
# 2.读取网址
# 3.翻译
# 4.找你需要的位置
# 5.保存

# import urllib.request
# from bs4 import BeautifulSoup
#
# # 找网址
# html = urllib.request.urlopen("https://pic.netbian.com/e/search/result/?searchid=2543")
# data = html.read()
# # print(data)
# soup = BeautifulSoup(data,"html.parser")
# # print(soup)
#
# imgurl = soup.find("div",attrs={"class":"wrap clearfix"})
# # print(imgurl)
# imgurl = imgurl.find("img")
# # print(imgurl)
#
# b = imgurl.get("src")
# # print(b)
#
# b = "https://pic.netbian.com"+b
#
# # print(b)
#
# urllib.request.urlretrieve(b,"muchen1.jpg")


# 多张图片


# import urllib.request
# from bs4 import BeautifulSoup
#
# # 1.打开网址
# html = urllib.request.urlopen("https://pic.netbian.com/e/search/result/?searchid=2543")
# data = html.read()
# # print(data)
# # 翻译内容
# con = BeautifulSoup(data,"html.parser")
#
# # 找位置
# a = con.find("ul",attrs={"class","clearfix"})
#
# # 找出所有的img标签
# img_all = a.find_all("img")
# # print(img_all)
# num = 1
# for i in img_all:
#     url = i.get("src")
#     # print(url)
#
#     url = "https://pic.netbian.com/"+url
#     print(url)
#
#     urllib.request.urlretrieve(url,"photo/%d.jpg"%num)
#     num+=1