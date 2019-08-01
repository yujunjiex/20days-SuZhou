# coding: UTF-8
"""
爬取search.creativecommons.org中的狗狗图片
"""

import json
import requests
import os
import random
import threading
from typing import List, Dict


train_path = 'trainData/'
test_path = 'testData/'

user_agent_list = [
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
    'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
    'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
]


def download_image(image_url, img_path, file_name):
    if not os.path.exists(train_path):  # 训练集
        os.mkdir(train_path)
    if not os.path.exists(test_path):  # 测试集
        os.mkdir(test_path)
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    filename = os.path.join(img_path, file_name)
    try:
        res = requests.get(image_url, timeout=8)
        if str(res.status_code)[0] == "4":
            return False
    except Exception as e:
        print(e)
        return False
    with open(filename, "wb") as f:
        f.write(res.content)
    return True


def craw(dog_name: str, begin_page: int, pages: int, order=1):
    """
    爬取狗狗的图片
    :param dog_name:  要爬取的狗狗名字
    :param begin_page: 爬取的起始页
    :param pages: 要爬取的页数(每页20张图片)
    :param order: 图片编号的起始值(默认为1)
    :return:
    """
    api = "https://api.creativecommons.engineering/image/search?page={}&shouldPersistImages=false&q={}"
    header = {
        'User-Agent': random.choice(user_agent_list),
        'Referer': 'search.creativecommons.org'
    }

    for page in range(begin_page, begin_page+pages+1):
        url = api.format(page, "+".join(dog_name.split()))
        resp = requests.get(url=url, headers=header)
        resp_json = resp.json()
        print("{}当前爬取页{}".format(threading.current_thread().name, page))
        for result in resp_json["results"]:
            if "thumbnail" in result:
                url = result["thumbnail"]
            elif "url" in result:   # 如果没有缩略图的话
                url = result["url"]
            else:
                continue
            file_name = str(order) + '.jpg'
            if download_image(url, train_path + dog_name, file_name):
                print("{}第{}张图片{}爬取成功!".format(threading.current_thread().name, order, url))
                order += 1
            else:
                print("{}{}爬取失败!!".format(threading.current_thread().name, url))


def begin_craw(dog_list: list, begin_page: object, order_list=None, pages=500):
    """程序入口(多线程方式爬取)"""
    if type(begin_page) is int:
        begin_page = [begin_page] * 6
    else:
        assert type(begin_page) is list and len(begin_page) == 6

    if order_list is None:
        order_list = [1] * 6
    threads = []

    for index, dog_name in enumerate(dog_list):
        thread = threading.Thread(target=craw, args=(dog_name, begin_page[index], pages, order_list[index]))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for t in threads:
        t.join()


if __name__ == '__main__':
    import time
    start = time.time()
    dog_list = ['Siberian Husky', 'Tibetan Mastiff', 'Golden Retriever', 'Bulldog', 'Poodle', 'German Shepherd dog']
    begin_craw(dog_list,
               begin_page=1,  # 用于应对中途ip被封或特殊情况
               order_list=None,
               pages=150)     # 每条狗爬250*20=5000张图片
    print("耗时:", time.time() - start)
    # download_image("https://c1.staticflickr.com/3/2233/2216381354_9db5e97f19_z.jpg?zz=1", train_path+"Siberian_Husky", "dog.jpg")

