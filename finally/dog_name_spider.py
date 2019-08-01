# coding: UTF-8
"""爬取133种狗的中文名"""
from glob import glob
import requests
from lxml import etree
from urllib import parse


def dog_english_name():
    dog_names = [item[60:-1] for item in sorted(glob("D:/PyCharm/cn-deep-learning/dog-project/dogImages/train/*/"))]
    res = []
    for dog_name in dog_names:
        res.append(dog_name.replace("_", " "))
    return res


def get_dog_name(dog_name):
    url_pc = "https://www.baidu.com/s"
    header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        "referer": "baidu.com"  # 关键(否则返回假数据)
    }
    url = "{}?wd={}&pn=0".format(url_pc, dog_name)   # 只爬第一页中的百度百科
    try:
        resp = requests.get(url, headers=header, timeout=6)
    except Exception as e:
        print("网络超时，重试,{}".format(e))
        return
    html = resp.content.decode("utf-8")

    baidu_urls = etree.HTML(html).xpath('//*[@id="content_left"]//div')

    for baidu_url in baidu_urls:
        url_info = baidu_url.xpath(".//@mu")
        if not url_info:
            continue
        else:
            url_info[0] = parse.unquote(url_info[0])
        if "baike.baidu.com" in url_info[0]:
            return url_info[0].split("/")[-2]

    return ""


if __name__ == '__main__':
    dog_english_name()
    dog_dict = {}
    for dog_name in dog_english_name():
        dog_dict[dog_name] = get_dog_name(dog_name)

    print(dog_dict)


