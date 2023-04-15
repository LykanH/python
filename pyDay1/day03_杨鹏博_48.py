# 将歌单信息用表格统计
# import csv
# with open("ge.csv","w",encoding="utf-8") as file:
#     f = csv.writer(file)
#     ge = ["歌名","歌手","专辑"]
#     f.writerow(ge)
#     neirong = [("a","b","c"),("a","b","c"),("a","b","c")]
#     f.writerows(neirong)

# 忠犬八公单页
# 电影分析

# import html5lib
# import urllib.request
# from bs4 import BeautifulSoup
# import requests
# import csv
# with open("mv.csv","a",encoding="utf-8",newline="") as file:
#     url = "https://movie.douban.com/subject/26999802/comments?sort=new_score&status=P"
#     head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"}
#     requ = requests.get(url,headers=head)
#     print(requ) #418
#     soup = BeautifulSoup(requ.content,"html.parser")
#     block = soup.find("div",attrs={"class","mod-bd"})
#     comment_all = block.find_all("div",attrs={"class","comment-item"})
#     f = csv.writer(file)
#     con = ["name","star","comment"]
#     f.writerow(con)
#     all_item = []
#     for i in comment_all:
#         name = i.find("a").get("title") #评论者名字
#         star = i.find("span",attrs={"class","rating"}).get("title")
#         print(star)
#         com = i.find("span",attrs={"class","short"}).text
#         item = (name,star,com)
#         all_item.append(item)
#     f.writerows(all_item)


# 忠犬八公多页爬取
# import html5lib
# from bs4 import BeautifulSoup
# import requests
# import csv
#
# with open("mv_echo_2.csv", "a", encoding="utf-8", newline="") as file:
#     num = 1
#     f = csv.writer(file)
#     con = ["name", "star", "comment"]
#     f.writerow(con)
#     all_item = []
#     while (num <= 20):    
#         if (num == 1):
#             url = "https://movie.douban.com/subject/35595615/comments?limit=20&status=P&sort=new_score"
#         else:
#             url = "https://movie.douban.com/subject/35595615/comments?start=%s&limit=20&status=P&sort=new_score" % str(
#                 (num - 1) * 20)
#         head = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"}
#         requ = requests.get(url, headers=head)
#         soup = BeautifulSoup(requ.content, "html.parser")
#         comment_all = soup.find_all("div", attrs={"class": "comment-item"})
#         for i in comment_all:
#             inf = i.find("span", attrs={"class": "comment-info"})
#             name = inf.find("a").text  # 用户名
#             star = inf.find("span", attrs={"class", "rating"})  # .text #评分
#             if star == None:
#                 star = "无星"
#             else:
#                 star = star.get("title")
#             comment = i.find("span", attrs={"class", "short"}).text
#             item = (name, star, comment)
#             print(item)
#             all_item.append(item)
#         num += 1  # 翻页
#     f.writerows(all_item)


# 柱状图
# def zhuzhuangtu():
#     line_chart = pygal.Bar()
#     line_chart.title = '忠犬八公'
#     asx = ["很差", "较差", '还行', "推荐", "力荐"]
#     m = 0
#     while(m<5):
#         cccc=asx[m]
#         print(cccc)
#         line_chart.add(cccc,count(cccc))
#         m+=1
#     line_chart.render_to_file('bagong.svg')


# 雷达图
# def leidatu():
#     radar_chart = pygal.Radar()
#     radar_chart.title = '忠犬八公'
#     asx = ["很差", "较差", '还行', "推荐", "力荐"]
#     m = 0
#     n = []
#     radar_chart.x_labels = ["很差", "较差", '还行', "推荐", "力荐"]
#     while(m<5):
#         cccc=asx[m]
#         n.append(count(cccc))
#         m+=1
#     print(n)
#     radar_chart.add('评分', n)
#     radar_chart.render_to_file('bagong.svg')

# 折线图
# def zhexiantu():
#     zhe_chart = pygal.Line()
#     zhe_chart.title = '忠犬八公'
#     asx = ["很差", "较差", '还行', "推荐", "力荐"]
#     zhe_chart.x_labels = map(str,asx)
#     m=0
#     t=[]
#     while(m<5):
#         acc = count(asx[m])
#         # print(acc)
#         t.append(acc)
#         m+=1
#     zhe_chart.add('龙马精神', t)
#     zhe_chart.render_to_file('bagong.svg')
# zhexiantu()