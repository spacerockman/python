import csv
import urllib.request
import re
from tqdm import tqdm

url = 'https://www.mjf2020.com/?s='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
sub_page_list = []
sub_page_list_1080 = []
# sub_page_magnet_list_1080 = []
count = 0

obj1 = re.compile(r'<h2 class="thumbnail">(?P<test1>.*?)'
                  r'<img src=.*?onmouseout="this.style.*? href="(?P<subUrl>.*?)>', re.S)

sub_page_reObj = re.compile(r'<ul class="vc_tta-tabs-list">.*?'
                            r'<li class="vc_tta-tab vc_active".*?'
                            r'<li class="vc_tta-tab" data-vc-tab><a href="(?P<subUrl_1080>.*?)" data-vc-tabs.*?1080p"', re.S)

sub_page_1080_reObj = re.compile(r'<p style="text-align: right;" alt="(?P<detailNames>.*?)" title=".*?'
                                 r'href="(?P<magnet>.*?)">磁力</a></p>', re.S)


print("输入你要搜索的剧名:")
show_name = input()
filename = '{}'.format(show_name)
filename_result = "/Users/xujintao/workspace/python/scrawler/" + filename + '.csv'
f = open(filename_result, mode="w", encoding="GBK")
csvWriter = csv.writer(f)
csvWriter.writerow(['名称', '下载链接'])


# 中文转义
show_name_quoted = urllib.parse.quote(show_name)
# 拼接url字符
result_url = '{}{}'.format(url, show_name_quoted)
# 设置请求
request = urllib.request.Request(result_url, headers=headers, method='GET')
# 发送请求
response = urllib.request.urlopen(request)
# 页面转码成UTF-8
result = response.read().decode("utf-8")

# 获取子页面的链接
sub_urls = obj1.finditer(result)
for sub_url in sub_urls:
    sub_page_list.append(sub_url.group('subUrl'))

for sub_url in sub_page_list:
    sub_request = urllib.request.Request(sub_url, headers=headers, method="GET")
    sub_response = urllib.request.urlopen(sub_request)
    sub_result = sub_response.read().decode('utf-8')
    result_1080 = sub_page_reObj.finditer(sub_result)
    for i in result_1080:
        count += 1
        sub_page_list_1080.append(sub_url+i.group('subUrl_1080'))

print('获取资源中...')
bar = tqdm(sub_page_list_1080)
for sub_url_1080 in bar:
    sub_1080_request = urllib.request.Request(sub_url_1080, headers=headers, method="GET")
    sub_1080_response = urllib.request.urlopen(sub_1080_request)
    sub_1080_results = sub_1080_response.read().decode('utf-8')
    result_1080_urls = sub_page_1080_reObj.finditer(sub_1080_results)
    for item in result_1080_urls:
        csvWriter.writerow(item.groupdict().values())

print("{}{}{}".format("资源获取完成，请查看: ", show_name, ".csv 文件"))
response.close()

