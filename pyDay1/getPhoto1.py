import urllib.request
from bs4 import BeautifulSoup

# 1.打开网址
html = urllib.request.urlopen("https://pic.netbian.com/e/search/result/?searchid=2543")
data = html.read()
# print(data)
# 翻译内容
con = BeautifulSoup(data,"html.parser")

# 找位置
a = con.find("ul",attrs={"class","clearfix"})

# 找出所有的img标签
img_all = a.find_all("img")
# print(img_all)
num = 1
for i in img_all:
    url = i.get("src")
    # print(url)

    url = "https://pic.netbian.com/"+url
    print(url)

    urllib.request.urlretrieve(url,"photo/%d.jpg"%num)
    num+=1
