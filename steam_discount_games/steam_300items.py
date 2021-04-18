import requests
import json
from pathlib import Path
import pandas as pd
import bs4
import re
import webbrowser

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
url_100 = "https://store.steampowered.com/search/results/?query&start=1&count=100&dynamic_data=&sort_by=_ASC&snr=1_7_7_2300_7&specials=1&filter=topsellers&infinite=1"
url_200 = "https://store.steampowered.com/search/results/?query&start=100&count=200&dynamic_data=&sort_by=_ASC&snr=1_7_7_2300_7&specials=1&filter=topsellers&infinite=1"
url_300 = "https://store.steampowered.com/search/results/?query&start=200&count=300&dynamic_data=&sort_by=_ASC&snr=1_7_7_2300_7&specials=1&filter=topsellers&infinite=1"
url_400 = "https://store.steampowered.com/search/results/?query&start=300&count=400&dynamic_data=&sort_by=_ASC&snr=1_7_7_2300_7&specials=1&filter=topsellers&infinite=1"


# 下载保存JSON文件
def saveJson100(url):
    # 读取url地址，
    response = requests.get(url, headers=headers)
    html_str = response.content.decode()

    # 加载数据,将Json数据转换成python类型(字典dict)
    result = json.loads(html_str)

    with open("url_100.json", "w", encoding="utf-8") as f:
        # 加一些参数，自动格式化
        f.write(json.dumps(result, ensure_ascii=False, indent=4))
    pass

# 下载保存JSON文件2


def saveJson200(url):
    # 读取url地址，
    response = requests.get(url, headers=headers)
    html_str = response.content.decode()

    # 加载数据,将Json数据转换成python类型(字典dict)
    result = json.loads(html_str)

    with open("url_200.json", "w", encoding="utf-8") as f:
        # 加一些参数，自动格式化
        f.write(json.dumps(result, ensure_ascii=False, indent=4))
    pass


def saveJson300(url):
    # 读取url地址，
    response = requests.get(url, headers=headers)
    html_str = response.content.decode()

    # 加载数据,将Json数据转换成python类型(字典dict)
    result = json.loads(html_str)

    with open("url_300.json", "w", encoding="utf-8") as f:
        # 加一些参数，自动格式化
        f.write(json.dumps(result, ensure_ascii=False, indent=4))
    pass

# 输出文档


def outputCSV_by_pd():
    data1 = {}
    data2 = {}
    data3 = {}
    applink = []
    #applink2 = []

    # path to file
    p1 = Path(r'./url_100.json')
    p2 = Path(r'./url_200.json')
    p3 = Path(r'./url_300.json')
    # read the JSON file in
    with p1.open('r') as f1:
        data1 = json.loads(f1.read())
    with p2.open('r') as f2:
        data2 = json.loads(f2.read())
    with p3.open('r') as f3:
        data3 = json.loads(f3.read())
    # 得到dom of data1
    searchSoup1 = bs4.BeautifulSoup(
        data1['results_html'], features="html.parser")
    # 得到dom of data2
    searchSoup2 = bs4.BeautifulSoup(
        data2['results_html'], features="html.parser")
    # 得到dom of data3
    searchSoup3 = bs4.BeautifulSoup(
        data3['results_html'], features="html.parser")
    # 获取折扣，游戏名称，游戏链接 of data1
    discount_elements = searchSoup1.select('.search_discount span')
    app_name = searchSoup1.select('.title')
    href_elements = searchSoup1.select('a')
    # 获取折扣，游戏名称，游戏链接 of data2
    discount_elements_data2 = searchSoup2.select('.search_discount span')
    app_name_data2 = searchSoup2.select('.title')
    href_elements_data2 = searchSoup2.select('a')
    # 获取折扣，游戏名称，游戏链接 of data3
    discount_elements_data3 = searchSoup3.select('.search_discount span')
    app_name_data3 = searchSoup3.select('.title')
    href_elements_data3 = searchSoup3.select('a')

    # 拼接游戏名称
    app_name.extend(app_name_data2)
    app_name.extend(app_name_data3)

    # 拼接链接
    # 1. 拼接游戏链接
    for i in range(len(href_elements)):
        applink.append(href_elements[i].get('href'))
    # 2. 拼接游戏链接data2
    for i in range(len(href_elements_data2)):
        applink.append(href_elements_data2[i].get('href'))
    # 3. 拼接游戏链接data3
    for i in range(len(href_elements_data3)):
        applink.append(href_elements_data3[i].get('href'))

    # 拼接折扣
    discount_elements.extend(discount_elements_data2)
    discount_elements.extend(discount_elements_data3)

    # 组成新数据表
    steam_list = pd.DataFrame(app_name, columns=["游戏名称"])
    steam_list = pd.concat(
        [steam_list, pd.DataFrame(applink, columns=['游戏链接'])], axis=1)
    steam_list = pd.concat(
        [steam_list, pd.DataFrame(discount_elements, columns=['游戏折扣'])], axis=1)
    steam_list.to_csv("steam.csv", index=False)


saveJson100(url_100)
saveJson200(url_200)
saveJson300(url_300)
outputCSV_by_pd()
