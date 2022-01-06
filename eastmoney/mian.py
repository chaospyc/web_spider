import random
import time
import pickle
from selenium import webdriver  # 导入webdriver包
from bs4 import BeautifulSoup  # 导入BeautifulSoup包
import re
import xlwt
# 如果某一步报异常就跳过
# 采用不断记录soup的形式
# 记录soup后在进行处理
baseurl = "http://guba.eastmoney.com/list,601318.html"
findSumPade = re.compile(r'data-page="(.*?)"')

findReadNumber = re.compile(r'<span class="l1 a1">(.*?)</span>') #找到评论人数
findRevierNumber = re.compile(r'<span class="l2 a2">(.*?)</span>')
findRevierLink = re.compile(r'<span class="l3 a3"><a href="(.*?)" title=')
findRevier = re.compile(r'title="(.*?)">')
findRevierName = re.compile(r'target="_blank">(.*?)</a>')
findTime = re.compile(r'<span class="l5 a5">(.*?)</span>')
savepath = "中金公司.xlsx"
# filePath = "C:\\Users\\chaos\\Desktop\\自然语言处理\\gubaData\\爬虫\\eastmoney\\601995\\"+str(i)+".txt"


def main():

    dataList = []
    SumPageInt = SumPage(baseurl)
    for i in range(SumPageInt):
    # for i in range(2,10):
        try:
            filePath = "C:\\Users\\chaos\\Desktop\\自然语言处理\\gubaData\\爬虫\\eastmoney\\601318\\" + str(i) + ".txt"
            with open(filePath, 'rb') as f:  # 打开文件
                html = pickle.load(f)  # 将二进制文件对象转换成 Python 对象
                subsoup = BeautifulSoup(html, 'html.parser')
                data = getData(subsoup)
                dataList.append(data)
        except Exception as e:
            print(e)
    print(dataList)
    tempData = []
    for i in range(len(dataList)):
        for j in range(len(dataList[i])):
            try:
                tempData.append(dataList[i][j])
            except Exception as e:
                print(e)
    saveData(tempData, savepath)


def getData(soup):
    datalist = []
    for item in soup.find_all('div', class_="articleh normal_post"):
        data = []
        # print(item)
        item = str(item)
        readNumber = re.findall(findReadNumber,item)[0]
        data.append(readNumber)
        revierNumber = re.findall(findRevierNumber,item)[0]
        data.append(revierNumber)
        revierLink = re.findall(findRevierLink, item)
        data.append(revierLink)
        revier = re.findall(findRevier,item)[0]
        data.append(revier)
        revierName = re.findall(findRevierName, item)[0]
        data.append(revierName)
        revierTime = re.findall(findTime, item)[0]
        data.append(revierTime)
        datalist.append(data)
    return datalist


def getSubLink(soup,baseUrl):
    SumPageStr = str(soup.find_all('a',class_="last_page")) #找到总的页数的标签
    SumPageInt = int(re.findall(findSumPade,SumPageStr)[0]) #转换成int
    subUrlList = []
    for i in range(2,SumPageInt+1): #进行SubLink拼接
        # http://guba.eastmoney.com/list,601995.html
        url = baseUrl[:-5] + '_' + str(i)+ baseUrl[-5:]
        subUrlList.append(url)
    return subUrlList


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
    # driver.quit()
    return soup


def askAllUrl(url):
    dataSoup = []
    driver = webdriver.Chrome()  # 设置一个chrome对象
    driver.implicitly_wait(3)  # 设置等待3秒后打开目标网页
    driver.get(url)  # 获得网页
    driver.implicitly_wait(1)  # 设置等待3秒后打开目标网页
    html = driver.page_source  # 获取网页的资源 类似于response.read()
    soup = BeautifulSoup(html, 'html.parser')
    SumPageInt = SumPage(soup)
    # print(type(soup))
    dataSoup.append(soup)
    for i in range(2,SumPageInt+1):
        filePath = "C:\\Users\\chaos\\Desktop\\自然语言处理\\gubaData\\爬虫\\eastmoney\\601995\\"+str(i)+".txt"
        try:
            nextpage = driver.find_element_by_partial_link_text('下一页')
            time.sleep(2+random.random())
            nextpage.click()
            html = driver.page_source  # 获取网页的资源 类似于response.read()
            subsoup = BeautifulSoup(html, 'html.parser')
            with open(filePath,'wb') as f:
                pickle.dump(subsoup, f)
        except Exception as e:
            print(e)
        break
    return dataSoup


def SumPage(url):
    dataSoup = []
    driver = webdriver.Chrome()  # 设置一个chrome对象
    driver.implicitly_wait(3)  # 设置等待3秒后打开目标网页
    driver.get(url)  # 获得网页
    driver.implicitly_wait(1)  # 设置等待3秒后打开目标网页
    html = driver.page_source  # 获取网页的资源 类似于response.read()
    soup = BeautifulSoup(html, 'html.parser')
    findSumPade = re.compile(r'data-page="(.*?)"')
    SumPageStr = str(soup.find_all('a', class_="last_page"))  # 找到总的页数的标签
    SumPageInt = int(re.findall(findSumPade, SumPageStr)[0])  # 转换成int
    return SumPageInt


def saveData(data,savepath):
    book = xlwt.Workbook(encoding="utf-8")  # 创建workbook 对象
    sheet = book.add_sheet('中金公司', cell_overwrite_ok=True)  # 创建工作表
    col = ["评论数", "点赞数", "Link","评价内容","评论者姓名","时间"]
    for i in range(0, 6):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(data)):
        print(f"第{i + 1}条")
        tempdata = data[i]
        for j in range(0, 6):
            sheet.write(i + 1, j, tempdata[j])  #
    book.save(savepath)


if __name__ == "__main__":
    main()