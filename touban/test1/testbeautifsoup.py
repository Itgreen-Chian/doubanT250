# -*- coding = utf-8 -*-
"""
beautifulsoup4:把复杂的html文档转换为复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4类
tag
navigablestring
beautifulsoup
comment
"""
from bs4 import BeautifulSoup
import re


file = open("./test2.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")  # 以html.parser方式解析html
# print(bs.title)
# print(bs.head)
# print(bs.a)
# print(type(bs.head))   # <class 'bs4.element.Tag'>
# 1、tag: 标签及标签内容，默认只取第一个数据 标签有属性可以单独提取属性

# print(type(bs.title.string))   # <class 'bs4.element.NavigableString'> 标签内容、字符串
# print(bs.title.string)

# 2、NavigableString:标签内容、字符串

# print(bs.a.attrs)  # 扩展：attrs 标签的所有属性会以字典的形式展示每一个属性

# print(type(bs))  # <class 'bs4.BeautifulSoup'>
# 3、BeautifulSoup：表示整个文档
# print(bs)  # 打印整个文档

# print(bs.a.string)
# print(type(bs.a.string))  # comment：注释
# 4、comment: 是一个特殊的navigablestring,输出的内容不包括注释

# -------------------------------------------------------
# 节点的获取
# 文档的遍历：把文档中相似的数据找到
# print(bs.head.contents)  # 遍历，会以列表的形式输出
# print(bs.head.contents[1])  # 通过下标取单个列表元素

# contents:获取tag的所有子节点，返回一个列表
# children 获取tag的所有子节点，返回一个生成器
# for child in bs.body.childeren:
#     print(child)
# descendants: 获取tag所有子孙节点
# strings 如果tag包含多个字符串，即在子孙节点中有内容，可以用此获取，而后遍历
# stripped_string: 用法和string一样，只不过滤掉那些空白内容
# parent: 获取父节点
# 更多内容所搜文档

# 文档的所搜
# 1、字符串过滤，会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# print(t_list)

# 2、正则表达式所搜，使用search()方法匹配内容
# t_list = bs.find_all(re.compile("a"))
# print(t_list)


# 3、传入一个函数（方法），根据函数要求来查找
# has_attr("name"):表示含有字符串“name”
# def name_is_exists(tag):
#     return tag.has_attr("name")


# t_list = bs.find_all(name_is_exists)
# print(t_list)
# for item in t_list:  # 以列表方式展示
#     print(item)

# 4、kwargs  参数
# t_list = bs.find_all(id="douban-logo")
# print(t_list)

# 5、text参数
# t_list = bs.find_all(text="豆瓣")
# for item in t_list:
#     print(item)

# t_list = bs.find_all(text=re.compile("\d"))  # 用正则表带是来查找包含特定文本内容（标签里的字符串）
# for item in t_list:
#     print(item)

# 5、limit参数：限定数据数量
# t_list = bs.find_all("a", limit=3)  # limit限制获取的数量（3)
# for item in t_list:
#     print(item)

# 6、css选择器
# t_list = bs.select('title')  # 通过标签查找
# t_list = bs.select('#v1')  # 通过id查找
# t_list = bs.select("a[class='ied']")  # 通过标签属性查找
# t_list = bs.select("head>title")  # 子标签查找
# t_list = bs.select('.anony-nav-links')  # 通过类查找
# t_list = bs.select(".mry ~ .yte")  # 兄弟标签 跟.mry同一层的.yte
# for item in t_list:
#
#     print(item)
