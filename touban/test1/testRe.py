# -*- coding = utf-8 -*-
# 正则表达式 字符串模式，判断字符串是否符合标准

import re


# 创建模式对象
# pat = re.compile("AA")  # AA是正则表达式，用来验证其他字符串
# m = pat.search("ABCAA")  # search被校验得内容
# print(m)  # None:不匹配  <re.Match object; span=(3, 5), match='AA'> SPAN(3,5)匹配到下标3、4符合

# 没有模式对象
# n = re.search("asc", "adascn")   # 前面的字符串是匹配规则，后一个字符串是校验对象
# print(n)

# print(re.findall("a", "bacdad"))  # ['a', 'a']
# print(re.findall("[A-Z]", "BaCdaD"))   # ['B', 'C', 'D'] [A-Z]:正则表达式规则
# print(re.findall("[A-Z]+", "BACdaD"))   # ['BAC', 'D']


# sub
# print(re.sub("a", "A", "abac"))  # 找到a用A替换，在第三个字符串中查找
# 建议在正则表达式中，被比较的字符串前面加上r，使字符串不用担心转移字符的问题
# a = r"ab\c"
# print(a)  # ab\c
