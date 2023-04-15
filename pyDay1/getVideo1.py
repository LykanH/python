import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.mercedes-benz.com.cn/vehicles/sedan/maybach-s-class.html"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"}

resp = requests.get(url,head)
# print(resp)
soup = BeautifulSoup(resp.content,"html.parser")
# print(soup)

# video = soup.find("video")

src = soup.find("div",attrs={"class","long-video__fullscreen-video-wrapper"})
# print(src)

video = "https://www.mercedes-benz.com.cn/"+src.find("video").get("data-src")
# print(video)

urllib.request.urlretrieve(video,"video/maybach.mp4")

# for i in video_all:
#     print(i)
#     a = i.get("src")
