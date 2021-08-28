import requests
import csv
import xml
import re

keyword = input("输入需要的资源名称（English only）：")

url = 'https://eztv.re/search/' + keyword
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.107 Mobile Safari/537.36 "
}
# 获得网页
response = requests.get(url, headers=header)

# 过滤获取
obj = re.compile(r'<td class="forum_thread_post">.*?'
                 r'title="(?P<title>.*?)" alt=".*?'
                 r'<td align="center" class="forum_thread_post">.*?'
                 r'<a href="(?P<magnet>.*?)" class="magnet".*?'
                 r'<font color="green">(?P<seed>.*?)</font>', re.S)

results = obj.finditer(response.text)
with open(keyword + '.csv', mode='w', encoding='GBK') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(['资源名称', 'magnet', '种子下载数'])
    for i in results:
        dic = i.groupdict()
        csvWriter.writerow(dic.values())

# print(response.text)
response.close()