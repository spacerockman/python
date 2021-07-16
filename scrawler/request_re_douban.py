import csv
import re

import requests

url = "https://movie.douban.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

res = requests.get(url, headers=header)
obj = re.compile(r'<ul class="">.*?<li class="title">.*?'
                 r'href="(?P<href>.*?)" class="">(?P<title>.*?)</a>.*?'
                 r'<span class="subject-rate">(?P<rating>.*?)</span>', re.S)

films = obj.finditer(res.text)

with open("data.csv", mode="w", encoding="GBK") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["链接", "电影名称", "评分"])
    for i in films:
        dic = i.groupdict()
        csvWriter.writerow(dic.values())

print("over")
f.close()
res.close()