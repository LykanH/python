# 翻页

# https://movie.douban.com/subject/35595615/comments?limit=20&status=P&sort=new_score
# https://movie.douban.com/subject/35595615/comments?start=20&limit=20&status=P&sort=new_score
# https://movie.douban.com/subject/35595615/comments?start=40&limit=20&status=P&sort=new_score

import html5lib
from bs4 import BeautifulSoup
import requests
import csv

with open("mv_echo_2.csv","a",encoding="utf-8",newline="") as file:
    num=1

    f = csv.writer(file)
    con = ["name","star","comment"]
    f.writerow(con)
    all_item = []


    while(num<=20):
        if(num==1):
            url = "https://movie.douban.com/subject/35595615/comments?limit=20&status=P&sort=new_score"
        else:
            url = "https://movie.douban.com/subject/35595615/comments?start=%s&limit=20&status=P&sort=new_score"%str((num-1)*20)

        head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"}
        # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34
        # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34
        requ = requests.get(url,headers=head)
        # print(requ)

        soup = BeautifulSoup(requ.content,"html.parser")

        comment_all = soup.find_all("div",attrs={"class":"comment-item"})
        for i in comment_all:
            inf = i.find("span",attrs={"class":"comment-info"})

            name = inf.find("a").text #用户名

            star = inf.find("span",attrs={"class","rating"}) #.text #评分
            if star == None:
                star="无星"
            else:
                star=star.get("title")
            comment = i.find("span",attrs={"class","short"}).text
    
            # print(name)
            # print(star)
            # print(comment)

            item = (name,star,comment)
            print(item)
            all_item.append(item)

        num+=1 # 翻页

    f.writerows(all_item)


