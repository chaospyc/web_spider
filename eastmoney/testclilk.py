import time

from selenium import webdriver  # 导入webdriver包
from bs4 import BeautifulSoup  # 导入BeautifulSoup包
import re
import xlwt

url = "http://guba.eastmoney.com/list,601995.html"
def askUrl(url):
    data = []
    driver = webdriver.Chrome()  # 设置一个chrome对象
    driver.implicitly_wait(3)  # 设置等待3秒后打开目标网页
    driver.get(url)  # 获得网页
    driver.implicitly_wait(1)  # 设置等待3秒后打开目标网页
    # element_re = driver.find_element_by_id('review-tag-num')  # 创建一个点击评论对象
    # element_re.click()  # 模拟点击评论
    html = driver.page_source  # 获取网页的资源 类似于response.read()
    soup = BeautifulSoup(html, 'html.parser')
    print(type(soup))
    data.append(soup)
    soup = str(soup)
    # sumpage = int(re.findall(findPage, soup)[-2])
    # print(sumpage)
    # 翻页功能，类名不能有空格，有空格可取后边的部分
    # nextpage = driver.find_element_by_class_name('ux-pager_btn__next') # 创建一个click对象
    # nextpage = driver.find_element_by_partial_link_text('下一页')
    for i in range(100):
        nextpage = driver.find_element_by_partial_link_text('下一页')
        time.sleep(3)
        nextpage.click()

    # driver.quit()
    return data

askUrl(url)