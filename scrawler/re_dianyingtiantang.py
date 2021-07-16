import re
import csv
import requests
import urllib3
import threading


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
domain = "https://www.dy2018.com/"

response = requests.get(domain)
response.encoding="gb2312"
obj1 = re.compile(r'2021必看热片.*?<ul>(?P<urls>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)

urlResult = obj1.finditer(response.text)
child_href_list = []

# 需要提前建立，不然每次都会新建一个data.csv，就会覆盖掉原来已经写入的数据
f = open("data.csv", mode="w", encoding="GBK")
csvWriter = csv.writer(f)
csvWriter.writerow(["电影简介链接", "电影名称", "下载链接"])

for i in urlResult:
    urls = i.group("urls")
    childUrlResults = obj2.finditer(urls)
    for hrefs in childUrlResults:
        hrefs = domain + hrefs.group("href").strip("/")
        child_href_list.append(hrefs)

# child page
for j in child_href_list:
    child_page_response = requests.get(j)
    child_page_response.encoding = "GBK"
    obj3 = re.compile(r'◎片　　名(?P<fileName>.*?)<br.*?'
                      r'#fdfddf"><a href="(?P<magnetLink>.*?)">magnet', re.S)
    child_page_result = obj3.finditer(child_page_response.text)
    for i in child_page_result:
        csvWriter.writerow(i.groupdict().values())

f.close()
response.close()