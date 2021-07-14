import json
import re
import requests

url = "https://movie.douban.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

res = requests.get(url, headers=header)
obj = re.compile('<ul class="">.*?<li class="title">.*?href="(?P<href>.*?)" class="">(?P<title>.*?)</a>', re.S)
# print(res.text)
res_json = []
films = obj.finditer(res.text)
for i in films:
    res_json.append(i.group("title"))
    res_json.append(i.group("href"))
    print(i.group("title"))
    print(i.group("href"))
res.close()