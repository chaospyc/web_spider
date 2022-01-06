import re

from bs4 import BeautifulSoup

file = open("zhongjing.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")

# print(bs.)
# 字符串过滤，会查找与字符串完全匹配的的内容
#找到lass_="l3 a3"的所有文本
# class="sumpage"
t_list = bs.find_all(class_="sumpage")
# re.compile("a")
finsumpage = re.match('\d')

# re.findall('\d',t_list)
print(type(t_list))