import time
import re
from selenium import webdriver  # 导入webdriver包
from bs4 import BeautifulSoup  # 导入BeautifulSoup包
import random
import pickle
import sys  # 导入sys模块


sys.setrecursionlimit(30000)  # 将默认的递归深度修改为30000

Sh50Number = [600036,601318,600016,601328,600000,601166,601088,600030,600519,600837,601601,601398,601668,600031,600585,600111,601006,601899,601939,600050,601169,601288,601857,600048,601989,600547,600900,600028,600348,600104,600089,601699,600019,600362,601600,600015,600383,601168,600489,601628,601766,600518,600999,601688,601958,601390,601919,601111,601818,601118]
baseSavePath = "C:\\Users\\chaos\\Desktop\\自然语言处理\\gubaData\\爬虫\\eastmoney\\数据包"
# baseUrl = "http://guba.eastmoney.com/list,601318.html"

def main():
    urlLinkListSh50 = urlLink()
    baseSP = savePath()
    for i in range(len(urlLinkListSh50)):
        askAllUrl(urlLinkListSh50[i],baseSP[i])


def savePath():
    savePathList = []
    for i in range(len(Sh50Number)):
        savePath = baseSavePath + "\\"+str(Sh50Number[i])+"\\"
        savePathList.append(savePath)
        print(savePath)
    return savePathList


def urlLink():
    urlLinkList = []
    for i in range(len(Sh50Number)):
        baseUrl = "http://guba.eastmoney.com/list,"+ str(Sh50Number[i])+".html"
        urlLinkList.append(baseUrl)
    return urlLinkList



def askAllUrl(url,savePath):
    dataSoup = []
    driver = webdriver.Chrome()  # 设置一个chrome对象
    driver.implicitly_wait(3)  # 设置等待3秒后打开目标网页
    driver.get(url)  # 获得网页
    driver.implicitly_wait(1)  # 设置等待3秒后打开目标网页
    html = driver.page_source  # 获取网页的资源 类似于response.read()
    soup = BeautifulSoup(html, 'html.parser')
    SumPageInt = SumPage(soup)
    print(type(soup))
    dataSoup.append(soup)
    for i in range(2,SumPageInt+1):
        filePath = savePath+str(i)+".txt"
        try:
            nextpage = driver.find_element_by_partial_link_text('下一页')
            time.sleep(2+random.random())
            nextpage.click()
            html = driver.page_source  # 获取网页的资源 类似于response.read()
            # subsoup = BeautifulSoup(html, 'html.parser')
            with open(filePath, 'wb') as f:
                pickle.dump(html, f)  # 这里保存的是html文件
        except Exception as e:
            print(e)
    driver.quit()


def SumPage(soup):
    findSumPade = re.compile(r'data-page="(.*?)"')
    SumPageStr = str(soup.find_all('a', class_="last_page"))  # 找到总的页数的标签
    SumPageInt = int(re.findall(findSumPade, SumPageStr)[0])  # 转换成int
    return SumPageInt




if __name__ == "__main__":
    main()