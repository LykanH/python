# 爬取铃声

import urllib.request
from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.jiduo.cc/liuxing/31419.html")
# print(html)

# print(html.content)

soup = BeautifulSoup(html.content,"html.parser")
# print(soup)

a = soup.find("div",attrs={"id":"pFile"}).text
print(a)

urllib.request.urlretrieve(a,"voice/vo_1.mp3")