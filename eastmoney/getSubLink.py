import re

from bs4 import BeautifulSoup
import xlwt
file = open("zhongjing.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
findSumPade = re.compile(r'data-page="(.*?)"')
# findLink =
# baseurl = "http://guba.eastmoney.com/list,601995.html"
def getSubLink(soup,baseUrl):
    SumPageStr = str(soup.find_all('a',class_="last_page")) #找到总的页数的标签
    SumPageInt = int(re.findall(findSumPade,SumPageStr)[0]) #转换成int
    subUrlList = []
    for i in range(2,SumPageInt+1): #进行SubLink拼接
        # http://guba.eastmoney.com/list,601995.html
        url = baseUrl[:-5] + '_' + str(i)+ baseUrl[-5:]
        subUrlList.append(url)

    return subUrlList


    # return int(SumPageStr)

# http://guba.eastmoney.com/list,601995.html
# http://guba.eastmoney.com/list,601995_2.html

findReadNumber = re.compile(r'<span class="l1 a1">(.*?)</span>')
findRevierNumber = re.compile(r'<span class="l2 a2">(.*?)</span>')
findRevierLink = re.compile(r'<span class="l3 a3"><a href="(.*?)" title=')
findRevier = re.compile(r'title="(.*?)">')
findRevierName = re.compile(r'target="_blank">(.*?)</a>')
findTime = re.compile(r'<span class="l5 a5">(.*?)</span>')
def getData(data):
    datalist = []
    for item in data.find_all('div', class_="articleh normal_post"):
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

def saveData(data,savepath):
    book = xlwt.Workbook(encoding="utf-8")  # 创建workbook 对象
    sheet = book.add_sheet('flash动画', cell_overwrite_ok=True)  # 创建工作表
    col = ("评论数", "点赞数", "Link","评价内容","评论者姓名","时间")
    for i in range(0, 6):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(data)):
        print(f"第{i + 1}条")
        tempdata = data[i]
        for j in range(0, 6):
            sheet.write(i + 1, j, tempdata[j])  #
    book.save(savepath)


print(getData(bs))

# print(getSubLink(bs,baseurl))