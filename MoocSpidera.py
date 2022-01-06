from selenium import webdriver  # 导入webdriver包
from bs4 import BeautifulSoup  # 导入BeautifulSoup包
import re  # 正则表达式
import xlwt  # 进行excel操作

findPage = re.compile(r'<a class="th-bk-main-gh">(.*)</a>')  # 设置找到一共有多少页评论的正则表达式
findName = re.compile(r'target="_top">(.*?)</a>')  # 找到姓名
findComment = re.compile(r'<span>(.*?)</span>')
findtime = re.compile(
    r'<div class="ux-mooc-comment-course-comment_comment-list_item_body_comment-info_time">发表于(.*?)</div>')


def main():
    url = "https://www.icourse163.org/course/HNU-1003037001"
    data = askUrl(url)
    data = getData(data)
    savepath = "高等数学.xls"
    saveData(data, savepath)
    print(data)
    # print(type(data[1])) #bs4.BeautifulSoup
    print('数据采集完成')


def getData(data):
    textData = []
    for i in data:
        for item in i.find_all('div', class_='ux-mooc-comment-course-comment_comment-list_item'):
            datalist = []  # 每一条评论的信息
            item = str(item)
            Name = re.findall(findName, item)[1]  # 添加姓名
            datalist.append(Name)
            comment = re.findall(findComment, item)[0]  # 添加评价内容
            datalist.append(comment)
            retime = re.findall(findtime, item)[0]
            retime = str(retime).replace(" ", "")
            datalist.append(retime)
            textData.append(datalist)
    return textData

    # print(type(i))


def saveData(data,savepath):
    book = xlwt.Workbook(encoding="utf-8")  # 创建workbook 对象
    sheet = book.add_sheet('flash动画', cell_overwrite_ok=True)  # 创建工作表
    col = ("姓名", "评价", "时间")
    for i in range(0, 3):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(data)):
        print(f"第{i + 1}条")
        tempdata = data[i]
        for j in range(0, 3):
            sheet.write(i + 1, j, tempdata[j])  #

    book.save(savepath)



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
    print(type(soup))
    data.append(soup)
    soup = str(soup)
    sumpage = int(re.findall(findPage, soup)[-2])
    # print(sumpage)
    # 翻页功能，类名不能有空格，有空格可取后边的部分
    nextpage = driver.find_element_by_class_name('ux-pager_btn__next') # 创建一个click对象
    for page in range(1, sumpage):
        print(f"第{page}页")
        driver.implicitly_wait(1)
        nextpage.click()
        html = driver.page_source
        eachSoup = BeautifulSoup(html, 'html.parser')
        data.append(eachSoup)
    driver.quit()
    return data


if __name__ == "__main__":
    main()
