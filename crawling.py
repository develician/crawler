import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.naver.com")

html = BeautifulSoup(data.text, "html.parser")

# print(html)
# print(data.text)
# test = html.select_one(".tb_tit")
# print(test)
#
# test2 = html.select(".bl_s")
# print(test2)

# ah_l = html.select_one("#hi")
# print(ah_l)

items = html.select(".ah_item .ah_a")
for item in items:
    rank = item.select_one(".ah_r").text
    keyword = item.select_one(".ah_k").text
    print(rank, keyword)