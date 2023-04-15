# 爬虫分析
# 1.找到你的网址，打开网址
# 2.读取网址
# 3.翻译
# 4.找你需要的位置
# 5.保存

import urllib.request
from bs4 import BeautifulSoup

# 1.找到网址，打开网址
html = urllib.request.urlopen("http://yangpengbo.top/")
# 2.读取网址
data = html.read()
# print(data)         #需要经过bs4翻译

# 翻译
soup = BeautifulSoup(data,"html.parser")
# print(soup)

# 4.找到所需的位置
imgurl = soup.find("img")
# print(imgurl)

imgurl="http://yangpengbo.top"+imgurl.get("src")
# print(imgurl)

# 保存
urllib.request.urlretrieve(imgurl,"muchen.jpg")