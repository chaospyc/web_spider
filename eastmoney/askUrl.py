from selenium import webdriver  # 导入webdriver包
from bs4 import BeautifulSoup  # 导入BeautifulSoup包
import re  # 正则表达式


def askUrl(url):
    data = []
    driver = webdriver.Chrome()  # 设置一个chrome对象
    driver.implicitly_wait(3)  # 设置等待3秒后打开目标网页
    driver.get(url)  # 获得网页
    driver.implicitly_wait(1)  # 设置等待3秒后打开目标网页
    element_re = driver.find_element_by_id('review-tag-num')  # 创建一个点击评论对象
    element_re.click()  # 模拟点击评论
    html = driver.page_source  # 获取网页的资源 类似于response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup
