import csv
from selenium import webdriver
import time

with open("jd2.csv","a",encoding="utf-8",newline="") as file:
    f = csv.writer(file)
    csv_head = ["name","price","store"]
    f.writerow(csv_head)
    all_item = []
    i = 1 # 表示每一页第几条
    j = 1 # 表示第几页
    wd = webdriver.Chrome(r"D:\社交\Google\chromedriver.exe")
    url = "https://www.jd.com"

    wd.get(url)
    # 放大窗口
    wd.maximize_window()

    # 输入搜索内容
    wd.find_element_by_css_selector("#key").send_keys("iphone8")
    # 点击搜索按钮
    wd.find_element_by_css_selector("#search > div > div.form > button").click()
    time.sleep(2)
    # J_bottomPage > span.p-num > a.curr
    # J_bottomPage > span.p-num > a.pn-next.disabled
    # J_bottomPage > span.p-num > a.pn-next
    # 滚轮下拉
    wd.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # J_goodsList > ul > li:nth-child(1)
    # J_goodsList > ul > li:nth-child(2)
    all_li = wd.find_elements_by_css_selector("#J_goodsList > ul > li")
    for li in all_li:
        # print(li)


        price = li.find_element_by_css_selector("div > div.p-price > strong > i").text
        # print(price)
        # J_comment_10056485243189
        # J_comment_10033282079592
        name = comment_num = li.find_element_by_css_selector("div > div.p-name.p-name-type-2 > a > em").text
        # print(name)

        # store = li.find_element_by_css_selector("div > div.p-shop > span > a").get_attribute("title")
        score = li.find_element_by_css_selector("div > div.p-shop > span > a").get_attribute("title")
        # print(store)
        all_item.append((name,price,score))
        print("当前第{}页，第{}条".format(j,i))
        i+=1
    # time.sleep(3)
    f.writerows(all_item)

    # wd.close()
