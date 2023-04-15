import pyecharts.options as opts
from pyecharts.charts import Pie
import csv
import pandas as pd

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=pie-doughnut

目前无法实现的功能:

1、迷之颜色映射的问题
"""
df = pd.read_csv("process.csv")
MyList = list(df["score"])

num_list = []
num1 = 0
num2 = 0
num3 = 0
num4  = 0
num5 = 0
def Count(num1,num2,num3,num4,num5):
    for i in range(0, len(MyList)):
        if(MyList[i]==1):
             num1 += 1
        elif(MyList[i]==2):
            num2 +=1
        elif(MyList[i]==3):
            num3 +=1
        elif(MyList[i]==4):
            num4 +=1
        elif(MyList[i]==5):
            num5 +=1
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
    num_list.append(num4)
    num_list.append(num5)

    return num_list
num_list = Count(num1,num2,num3,num4,num5)


x_data = ["一星", "二星", "三星", "四星", "五星"]
y_data = num_list
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])

(
    Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
    .add(
        series_name="访问来源",
        data_pair=data_pair,
        rosetype="radius",
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Customized Pie",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("customized_pie.html")
)
