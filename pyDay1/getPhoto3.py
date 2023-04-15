# 用requests爬取网站内容

import requests
import urllib.request
from bs4 import BeautifulSoup

# html = urllib.request.urlopen("https://www.pexels.com/zh-cn/search/wallpaper/")
# data = html.read()
# print(data)

url = "http://bizhi360.com/desk/"

resp = requests.get(url)
# print(resp)
# print(resp.content)

soup = BeautifulSoup(resp.content,"html.parser")
# print(soup)

content = soup.find("div",attrs={"class":"pic-list"})
# print(content)

img = content.find_all("img")
# print(img)

num = 1
for i in img:
    # print(i)
    src = i.get("src")
    print(src)
    urllib.request.urlretrieve(src,"photo_1/img%d.jpg"%num)
    num+=1