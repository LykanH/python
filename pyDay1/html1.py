from selenium import webdriver
import time

# 创建网页驱动对象
wd = webdriver.Chrome(r"D:\社交\Google\chromedriver.exe")
url = "https://www.baidu.com/"
wd.get(url)
wd.maximize_window()

wd.find_element_by_css_selector("#kw").send_keys("vultr")
wd.find_element_by_css_selector("#su").click()

time.sleep(3)
wd.close()
# # wd.find_element_by_id("#input")
# wd.find_element_by_css_selector("#input").send_keys("周杰伦")
# time.sleep(3)
# wd.find_element_by_css_selector("#icon").click()
