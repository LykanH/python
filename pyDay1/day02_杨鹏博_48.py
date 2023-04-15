# 用requests爬图片

# import requests
# import urllib.request
# from bs4 import BeautifulSoup
#
# # html = urllib.request.urlopen("https://www.pexels.com/zh-cn/search/wallpaper/")
# # data = html.read()
# # print(data)
#
# url = "http://bizhi360.com/desk/"
#
# resp = requests.get(url)
# # print(resp)
# # print(resp.content)
#
# soup = BeautifulSoup(resp.content,"html.parser")
# # print(soup)
#
# content = soup.find("div",attrs={"class":"pic-list"})
# # print(content)
#
# img = content.find_all("img")
# # print(img)
#
# num = 1
# for i in img:
#     # print(i)
#     src = i.get("src")
#     print(src)
#     urllib.request.urlretrieve(src,"photo_1/img%d.jpg"%num)
#     num+=1


# import requests
# import urllib.request
# from bs4 import BeautifulSoup
# url = "https://www.cgwallpapers.com/"
# hh = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"}
# resp = requests.get(url=url)
# # print(resp.content)
# soup = BeautifulSoup(resp.content,"html.parser")
# # print(soup)
# a= soup.find_all("img",attrs={"class":"zoom123"})
# for i in a:
#     # print(i)
#     b= i.get("src")
#     # print(b)
#     url = "https://www.cgwallpapers.com/"+b
#     print(url)

#import urllib.request
# from bs4 import BeautifulSoup
# html = urllib.request.urlopen("http://qianye88.com/")
# data = html.read()
# soup = BeautifulSoup(data,"html.parser")
# # print(soup)
# a = soup.find_all("div",attrs={"class":"item"})
# # print(a)
# b = soup.find_all("img")
# # print(b)
# num =1
# for i in b:
#     url = i.get("data-original")
#     print(url)
#     urllib.request.urlretrieve(url, "xxx/%d.jpg" %num)
#     num+=1

# 爬视频
# import requests
# from bs4 import BeautifulSoup
# import urllib.request
#
# url = "https://www.mercedes-benz.com.cn/vehicles/sedan/maybach-s-class.html"
# head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"}
#
# resp = requests.get(url,head)
# soup = BeautifulSoup(resp.content,"html.parser")
# src = soup.find("div",attrs={"class","long-video__fullscreen-video-wrapper"})
#
# video = "https://www.mercedes-benz.com.cn/"+src.find("video").get("data-src")
#
# urllib.request.urlretrieve(video,"video/maybach.mp4")


#4 前50章小说
import requests
import html5lib
from bs4 import BeautifulSoup
# resp = requests.get("https://www.bbiquge.net/book/84680/53762966.html")
# # print(resp)
# soup = BeautifulSoup(resp.content,"html5lib")
# # print(soup)
# title = soup.find("h1").text
# # print(title)
# content = soup.find("div",attrs={"id":"content"}).text.replace("笔趣阁 www.bbiquge.net，最快更新斗罗大陆V重生唐三最新章节！","").replace("    ","\n")
# # print(content)
# with open("斗罗大陆.txt","w",encoding="utf-8") as f:
#     f.write(title + "\n")
#     f.write(content)

# 整本小说
# import requests
# import html5lib
# from bs4 import BeautifulSoup
#
# def txt(url):
#     resp = requests.get(url)
#     # print(resp)
#     soup = BeautifulSoup(resp.content, "html5lib")
#     # print(soup)
#     title = soup.find("h1").text
#     # print(title)
#     content = soup.find("div", attrs={"id": "content"}).text.replace(
#         "笔趣阁 www.bbiquge.net，最快更新斗罗大陆V重生唐三最新章节！", "").replace("    ", "\n")
#     # print(content)
#     with open("斗罗大陆2.txt", "a", encoding="utf-8") as f:
#         f.write(title + "\n")
#         f.write(content+"\n")
# import requests
# from bs4 import BeautifulSoup
# import html5lib
# from day2 import *
# resp = requests.get(url="https://www.bbiquge.net/book/84680/")
# # print(resp)
# soup = BeautifulSoup(resp.content,"html5lib")
# # print(soup)
# a = soup.find_all("dd")
# # print(a)
# for i in a:
#     b = i.find("a")
#     # print(b)
#     c = "https://www.bbiquge.net/book/84680/"+b.get("href")
#     # print(c)
#     txt(c)
# x =2
# while(x<12):
#     g = requests.get(url="https://www.bbiquge.net/book/84680/index_%d.html"%x)
#     # print(resp)
#     h = BeautifulSoup(resp.content, "html5lib")
#     # print(soup)
#     j = soup.find_all("dd")
#     # print(a)
#     for k in j:
#         q = k.find("a")
#         # print(b)
#         r = "https://www.bbiquge.net/book/84680/" + q.get("href")
#         # print(c)
#         txt(r)
