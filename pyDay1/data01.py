import csv
from selenium import webdriver
import time

wd=webdriver.Chrome(r"D:\社交\Google\chromedriver.exe")

url="https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9F%8E%E5%B8%82%E4%BA%BA%E5%8F%A3%E6%8E%92%E5%90%8D%E8%A1%A8/16620508"
wd.get(url)

wd.maximize_window()
# wd.find_element_by_css_selector()
#
# wd.find_element_by_css_selector("#key").send_keys("")
#
# wd.find_element_by_css_selector("#search > div > div.form > button").click()
#
# time.sleep(2)
# 下滑操作
#
wd.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# time.sleep(3)
# body > div.body-wrapper > div.content-wrapper > div > div.main-content.J-content > table:nth-child(26)
# body > div.body-wrapper > div.content-wrapper > div > div.main-content.J-content > table:nth-child(27)
# body > div.body-wrapper > div.content-wrapper > div > div.main-content.J-content > table:nth-child(26)
#body > div.body-wrapper > div.content-wrapper > div > div.main-content.J-content > table:nth-child(32)
# # 精准定位区间
total = wd.find_element_by_css_selector("body > div.body-wrapper > div.content-wrapper > div > div.main-content.J-content")
#
# print(total)
# int num = 32
all = []
for i in range (26,33):
    li_all = total.find_elements_by_css_selector("table:nth-child(%d)"%i)

    # body > div.body - wrapper > div.content - wrapper > div > div.main - content.J - content > table: nth - child(
    #     26) > tbody > tr:nth - child(3)
    # body > div.body - wrapper > div.content - wrapper > div > div.main - content.J - content > table: nth - child(
    #     26) > tbody > tr:nth - child(4)
    data = li_all.find_elements_by_css_selector("tr")
    for j in data:
        print(j)
    # print(li_all)
    # all.append(li_all)
# for li in li_all:
#     print(li)
#     price=li.find_element_by_css_selector("div > div.p-price > strong > i").text
#     # print(price)
#     # J_goodsList > l > li:nth-child(1) > div > div.p-name.p-name-type-2 > a > em
#     brand=li.find_element_by_css_selector("div > div.p-name.p-name-type-2 > a > em").text#
#     # print(brand)# J_goodsList > ul > li:nth-child(1) > div > div.p-shop > span > aa").get_attribute("title")
#     store = li.find_element_by_css_selector("div > div.p-shop > span > a").get_attribute("title")
#     # print(store)
#     #
#     # with open("男士衣服.csv","a",encoding="utf-8",newline="") as file: