# 电影分析

import html5lib
import urllib.request
from bs4 import BeautifulSoup
import requests
import csv

with open("mv.csv","a",encoding="utf-8",newline="") as file:

    url = "https://movie.douban.com/subject/26999802/comments?sort=new_score&status=P"
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"}
    requ = requests.get(url,headers=head)
    print(requ) #418
    soup = BeautifulSoup(requ.content,"html.parser")
    # print(soup)

    block = soup.find("div",attrs={"class","mod-bd"})
    # print(block)

    comment_all = block.find_all("div",attrs={"class","comment-item"})

    f = csv.writer(file)
    con = ["name","star","comment"]
    f.writerow(con)
    all_item = []
    star_1 = 0 # 很差个数
    star_2 = 0 # 较差
    star_3 = 0 # 还行
    star_4 = 0 # 推荐
    star_5 = 0 # 力荐

    for i in comment_all:
        # print(i)
        name = i.find("a").get("title") #评论者名字
        # print(name)

        star = i.find("span",attrs={"class","rating"}).get("title")

        if(star == "力荐"): star_5+=1
        elif(star == "推荐"): star_4+=1
        elif(star == "还行"): star_3+=1
        elif(star == "较差"): star_2+=1
        else:star_1+=1
        print(star)

        com = i.find("span",attrs={"class","short"}).text
        # print(com)
        # i.find("span",attrs={"class","allstar40 rating"})

        item = (name,star,com)
        # print(item)
        all_item.append(item)
    f.writerows(all_item)
    # print(all_item)

    # print("很差:"+star_1+" 较差:"+star_2+" 还行:"+star_3+" 推荐:"+star_4+" 力荐:"+star_5)
