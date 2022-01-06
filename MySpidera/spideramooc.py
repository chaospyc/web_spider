# -*- codeing = utf-8 -*-

import sys
import re  # 正则表达式
from bs4 import BeautifulSoup  # 网页解析 星系获取
import xlwt  # 进行excel操作
import urllib.request, urllib.error  # 进行URL操作
import sqlite3  # 数据库操作

def main():

    baseurl = "https://search.51job.com/list/090200,000000,0000,03,9,99,%25E7%2590%2586%25E8%25B4%25A2%25E9%25A1%25BE%25E9%2597%25AE,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    datalist = getData(baseurl) # 爬取数据

    savepath = "上海师范大学英语语音.xls" # 保存数据

    saveData(datalist, savepath)


def getData(baseurl):
    datalist = []
    url = baseurl
    html = askURL(url)


def askURL(url):
   #  head = {
   #  "authority": "www.icourse163.org",
   #  "method":"POST",
   #  "path":"/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=4896a59690d545e781a3fe56c1ea68b9",
   # "scheme": "https",
   #  "accept": "* / *",
   #  "accept-encoding": "gzip,deflate, br",
   #  "accept-language": "zh-CN,zh;q = 0.9",
   #  "content-length": "47",
   #  "content-type": "application/x-www-form-urlencoded",
   #  "cookie": "EDUWEBDEVICE=2d5429c51b4947b59eaf5a2d397233a7;WM_TID = hrsb0K2VQLFFABFQQQN % 2BnAFLcEkowthf;__yadk_uid = hWK8n3QPwBuhMA6y1AEsS2A8wEQosQcW;    hasVolume = true;    videoVolume = 0.8; videoRate = 2;    hb_MA - A976 - 948    FFA05E931_source = cn.bing.com;    NTESSTUDYSI = 4896    a59690d545e781a3fe56c1ea68b9;    Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b = 1631022552, 1631082546, 1631089709, 1631149396;    Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b = 1631153133;    WM_NI = zr % 2    BzS6W5hdhG5qmKP9Kj4W1PnAfTjuYLT4r4OvHMtMo9q % 2    FVOcFHeodR % 2    FIx7cCZ5a33oBLj84CJr17r9cSU5RvCtf58fdMrO3WXLsM9WXiLHPSSIkdk9fBMbtdTh7Zjtidms % 3    D;    WM_NIKE = 9ca17ae2e6ffcda170e2e6ee97d040f2b0ffd7b25fed968bb2d85f838b8aaff439f59c9eccc949a1eefeaee72af0fea7c3b92abaaee59bd23e95eba885eb4df7afa3acd33389b6fcb8b45cae9faab5e97f9b949cd5f1408daa88aef747ade7bfd0d545a19a8886ee7092f18799b6698186fb82b239ad9e848bbb408196bed2b67afbbd9db6b85ab69dbc87b834a6bc8393ce3995888494d0339588a7adcb5c918d878ce761fbba8eaee180a88ca8d8d962b8b7ac8ef237e2a3",
   #  "origin": "https: // www.icourse163.org",
   #  "referer": "https: // www.icourse163.org / course / NUDT - 9004?outVendor = zw_mooc_pcsybzkcph_",
   #
   #  "sec - ch - ua - mobile": "?0",
   #  "sec - ch - ua - platform": "Windows",
   #  "sec - fetch - dest": "empty",
   #  "sec - fetch - mode": "cors",
   #  "sec - fetch - site": "same - origin",
   # "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 93.0.4577.63Safari / 537.36}"}
   # "sec-ch-ua":'"Google Chrome";v = "93"," Not;A Brand"; v = "99","Chromium"; v = "93"'
    head = {"user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 93.0.4577.63Safari / 537.36}"}

    request = urllib.request.Request(url, headers=head,method="POST")
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    print(html)
    return html


def saveData(datalist, savepath):  # 保存数据
    pass




if __name__ == "__main__":
    main()
