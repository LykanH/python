import urllib.request
from bs4 import BeautifulSoup


# 获得链接
html = urllib.request.urlopen("https://desk.duba.com/")
data = html.read()
# print(data)

# 解析网站内容
soup = BeautifulSoup(data,"html.parser")
# print(soup)

tar = soup.find("div",attrs={"class":"page-pc"})
# tar = tar.find("div",attrs={"class":"swiper-container main-swiper swiper swiper-container-initialized swiper-container-horizontal"})
tar = tar.find_all("video")

num = 1
for i in tar:
    src = i.get("src")
    urllib.request.urlretrieve(src,"yuanqi/%d.mp4"%num)
    num+=1