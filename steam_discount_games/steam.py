import requests
import json
from pathlib import Path
import pandas as pd
import bs4
import re
import webbrowser

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
url = "https://store.steampowered.com/search/results/?query&start=100&count=100&dynamic_data=&sort_by=_ASC&snr=1_7_7_2300_7&specials=1&filter=topsellers&infinite=1"
jsonpath = "./steam"


# 下载保存JSON文件
def saveJson():
    # 读取url地址，
    response = requests.get(url, headers=headers)
    html_str = response.content.decode()

    # 加载数据,将Json数据转换成python类型(字典dict)
    result = json.loads(html_str)

    with open("steam.json", "w", encoding="utf-8") as f:
        # 加一些参数，自动格式化
        f.write(json.dumps(result, ensure_ascii=False, indent=4))
    pass


# 输出文档
def outputCSV_by_pd():
    data = {}
    applink = []

    # path to file
    p = Path(r'./steam.json')
    # read the JSON file in
    with p.open('r') as f:
        data = json.loads(f.read())

    # 得到dom
    searchSoup = bs4.BeautifulSoup(
        data['results_html'], features="html.parser")
    # 获取折扣，游戏名称，游戏链接
    discount_elements = searchSoup.select('.search_discount span')
    app_name = searchSoup.select('.title')
    href_elements = searchSoup.select('a')

    # 拼接游戏链接
    for i in range(len(href_elements)):
        applink.append(href_elements[i].get('href'))

    # 组成新数据表
    steam_list = pd.DataFrame(app_name, columns=["游戏名称"])
    steam_list = pd.concat(
        [steam_list, pd.DataFrame(applink, columns=['游戏链接'])], axis=1)
    steam_list = pd.concat(
        [steam_list, pd.DataFrame(discount_elements, columns=['游戏折扣'])], axis=1)
    steam_list.to_csv("steam.csv", index=False)


saveJson()
outputCSV_by_pd()
