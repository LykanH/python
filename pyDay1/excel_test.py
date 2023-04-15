# 表格读写操作
import csv

with open("lisen.csv","w",encoding="utf-8",newline="") as file:
    f=csv.writer(file)
    con = ["剧名","男主","女主","类型"]
    f.writerow(con)
    content = [("狂飙","钢琴曲","爱心","悬疑"),("狂飙","钢琴曲","爱心","悬疑"),("狂飙","钢琴曲","爱心","悬疑"),("狂飙","钢琴曲","爱心","悬疑")]
    f.writerows(content)
