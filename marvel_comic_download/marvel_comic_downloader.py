from logging import exception
from urllib import response
import urllib.request
import os
import re
import urllib
import wget


# url_origin = "https://comiconlinefree.net/ms-marvel-2014/issue-"
url_origin = input("input the target comic:")
url_origin = f"https://comiconlinefree.net/{url_origin}/issue-"
episode_amount = 1000
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
jpg_links = []
current_path = "/Volumes/Public/Nas_Xujintao/Download/comics/"

jpg_link_re = re.compile(
    r'<img id="main_img" class="chapter_img" src="(?P<imgs>.*?)" alt', re.S)


# set request
def set_request(url):
    request = urllib.request.Request(url, headers=headers, method='GET')
    return request


# get web source code
def get_web_soucecode(request):
    response = urllib.request.urlopen(request)
    pages_amount_re = re.compile(
        r'<div class="label">of (?P<nums>.*?)<\/div>', re.S)
    response = response.read().decode('utf-8')
    pages_amount = pages_amount_re.findall(response)[0]
    return response, pages_amount


def get_chapter_create_directory(response, current_path):
    chapter_re = re.compile(
        r'.*<span class="mi-title">(?P<chapter>.*?) Release Information:</span><br>', re.S)
    chapter = chapter_re.findall(response)[0]
    path = f'{current_path}/{chapter}'
    isExit = os.path.exists(path)
    if(isExit is False):
        os.mkdir(path)
    return path


try:
    # Download a series of comics
    for i in range(episode_amount + 1):
        if i > 0:
            url = f"{url_origin}{i}"
            print(url)
            request = set_request(url)
            response, pages_amount = get_web_soucecode(request)
            path = get_chapter_create_directory(response, current_path)
            pages_amount = int(pages_amount)

            links_list = []
            # get all page links
            for j in range(pages_amount+1):
                if j != 0:
                    links_list.append(f"{url}/{j}")

            for index, z in enumerate(links_list):
                print(z)
                request = set_request(z)
                res, pages_amount = get_web_soucecode(request)
                jpg_link = jpg_link_re.findall(res)[0]
                wget.download(jpg_link, out=path)

            url = f"{url_origin}"
except Exception as e:
    print("===================================================")
    print(e)
    print("===================================================")
