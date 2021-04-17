import json
import sys
import requests
import collections
import csv
from pathlib import Path
import pandas as pd


# 头部
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36"
}
url = "https://store.steampowered.com/broadcast/ajaxgetpopularpartnerbroadcasts/?minviews=1&tagid=0&genreid=37&categoryid=0&maxbroadcasts=12"
jsonpath = "./steam"


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


# 自动打开JSON文件，可忽略
def openJson():
    with open("steam.json", "r", encoding="utf-8") as f:
        # 读取数据
        res = f.read()
        # 加载
        my = json.loads(res)
        print(my)

        # 字典
        # print(type(my))
    pass


# 输出文档
def outputCSV_by_pd():
    # path to file
    p = Path(r'./steam.json')
    # read the JSON file in
    with p.open('r') as f:
        data = json.loads(f.read())
    # create the dataframe
    df_filtered = pd.DataFrame.from_dict(data['filtered'])

    # create a new dataframe
    df_appname_applink = pd.DataFrame.from_dict(df_filtered['app_name'])

    # inster into df_appname_applink dataframe
    df_appname_applink.insert(1, 'app_link', df_filtered['app_link'])
    print(df_appname_applink)
    # save to csv
    df_appname_applink.to_csv('steam.csv', index=False)


# 执行保存最新JSON
saveJson()

# 执行输出文档
outputCSV_by_pd()
