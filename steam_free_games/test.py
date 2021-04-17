import json
import requests
# 头部
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36"
}

# url地址
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
response = requests.get(url, headers=headers)
html_str = response.content.decode()
# print(html_str)


# 加载数据,将Json数据转换成python类型(字典dict)
result = json.loads(html_str)
# print(result)

# 写入
with open("douban.json", "w", encoding="utf-8") as f:

    # 如果是字典，就不能直接使用的哦！发生异常：TypeError: write() argument must be str, not dict
    # f.write(result)

    # 解决(1)：必须用json.dumps 把python转换成json字符串
    # f.write(json.dumps(result))
    # 加一些参数，自动格式化
    f.write(json.dumps(result, ensure_ascii=False, indent=4))

    # 解决(2): 也可以直接转换成字符串
    # f.write(str(result))
    pass


with open("douban.json", "r", encoding="utf-8") as f:
    # 读取数据
    res = f.read()
    # 加载
    my = json.loads(res)
    print(my)
    # 字典
    # print(type(my))
