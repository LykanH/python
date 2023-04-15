# 翻页数据分析

import csv

def getData():
    comment_all = []
    star = ["很差","较差","还行","推荐","力荐"]
    with open("mv_echo_1.csv","r",encoding="utf-8") as file:
        con = csv.reader(file)
        # print(con)

        for i in con:
            # print(i[1])
            if i[1] not in star:
                continue
            else:
                comment_all.append(i[1])
    return comment_all

print(getData())

def star_getCount(star):
    data = getData()
    count = 0
    for i in data:
        if i == star:
            count+=1
        else:
            continue
    return count

a = star_getCount("很差")
print(a)