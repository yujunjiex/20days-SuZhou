# coding: UTF-8
"""
模拟登陆长江大学官网
"""
import requests
import re
import execjs
import random
from time import sleep

host = "http://jwc3.yangtzeu.edu.cn/"
login_url = "http://jwc3.yangtzeu.edu.cn/eams/login.action"
target_url = "http://jwc3.yangtzeu.edu.cn/eams/home.action"

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

cjdx_session = requests.session()   # 因为同一个sessionid下的8-4-4-12uuid是保存在服务器端的，任一uuid都可登陆


def get_main_page(url, page_coding="utf8"):
    """获取登陆页面的html"""
    header = {'User-Agent': random.choice(user_agent_list)}
    html = cjdx_session.get(
                url,
                headers=header,
                timeout=6
                )
    return html.content.decode(page_coding)


def parse_password(html_page: str, password: str) -> str:
    """对password进行sha1哈希加密"""
    pattern = re.compile(r"CryptoJS.SHA1\('+[\S*]+' \+ form\['password'\].value\)")
    url = pattern.findall(html_page)[0]
    url = url.replace("CryptoJS.SHA1('", "")
    url = url.replace("' + form['password'].value)", "")
    try:
        with open("./sha1.js", 'r', encoding="utf8") as f:
            js_str = f.read()
    except Exception as e:
        print("文件{}读出错,{}".format("execSha1.js", e))
    js = execjs.compile(js_str)  # 编译执行js代码
    return js.call('parsePasswd', url + password)


def login(username, password):
    # TODO: 处理页面中的ajax
    params = {
        "username": username,
        "password": parse_password(get_main_page(login_url), password)
    }
    sleep(2)    # 等待两秒，否则页面提示不要过快点击
    header = {
        'User-Agent': random.choice(user_agent_list),
        'Referer': 'http://jwc3.yangtzeu.edu.cn/eams/home.action'
        }
    try:
        resp = cjdx_session.post(login_url, data=params,
                                 headers=header,
                                 timeout=6)
    except TimeoutError:
        print("登陆超时，请检查网络")
        return

    # ajax加载的页(session.get获取即可)
    menu_url = host + "eams/home!submenus.action"
    welcome_url = host + "eams/home!welcome.action"
    # TODO: 如果要获取ajax异步加载后的页面，可以用selenium模拟

    with open('login1.html', 'wb') as f:
        f.write(resp.content)
    cjdx_cookie = resp.cookies.get_dict()
    print(cjdx_cookie)
    sleep(2)    # 等待两秒，否则页面提示不要过快点击
    resp_data = cjdx_session.get(target_url, headers=header, cookies=cjdx_cookie)
    with open('login2.html', 'wb') as f:
        f.write(resp_data.content)
        print('登录成功')


if __name__ == '__main__':
    login("201602565", "201602565")
    # parse_password(get_main_page(target_url), "123")
