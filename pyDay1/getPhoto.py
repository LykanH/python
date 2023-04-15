# 爬虫分析
# 1.找到你的网址，打开网址
# 2.读取网址
# 3.翻译
# 4.找你需要的位置
# 5.保存

import urllib.request
from bs4 import BeautifulSoup

# 找网址
html = urllib.request.urlopen("https://pic.netbian.com/e/search/result/?searchid=2543")
data = html.read()
# print(data)
soup = BeautifulSoup(data,"html.parser")
# print(soup)

imgurl = soup.find("div",attrs={"class":"wrap clearfix"})
# print(imgurl)
imgurl = imgurl.find("img")
# print(imgurl)

b = imgurl.get("src")
# print(b)

b = "https://pic.netbian.com"+b

# print(b)

urllib.request.urlretrieve(b,"muchen1.jpg")