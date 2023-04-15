import requests

resp=requests.get("https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js").json()
print(resp)