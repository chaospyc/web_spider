# -*- codeing = utf-8 -*-

import sys
import re  # 正则表达式
from bs4 import BeautifulSoup  # 网页解析 星系获取
import xlwt  # 进行excel操作
import urllib.request, urllib.error  # 进行URL操作
import sqlite3  # 数据库操作


def main():
    url = "https://www.icourse163.org/web/j/recommendRPCBean.getRecommend.rpc?csrfKey=4896a59690d545e781a3fe56c1ea68b9"
    html = askUrl(url)

def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

    requests = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    print(html)
    return html





if __name__ == "__main__":
    main()
