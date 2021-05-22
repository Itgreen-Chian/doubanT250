# -*- coding: utf-8 -*-
import sqlite3

"""
创建数据库
# conn = sqlite3.connect("test.db")  # 打开或创建数据库
# print("Open database successful")
"""

"""
创建数据表
conn = sqlite3.connect("test.db")  # 打开或创建数据库
print("Open database successful")
c = conn.cursor()   # 获取游标

sql = '''
    create table company
    (id int not null,
    name text not null,
    age int not null,
    address char(50),
    salary real);
'''
c.execute(sql)  # 执行sql语句
conn.commit()   # 提交数据库操作语句
conn.close()    # 关闭数据库
print("成功建表")
"""

"""
# 插入数据
conn = sqlite3.connect("test.db")  # 打开或创建数据库
# print("Open database successful")
c = conn.cursor()   # 获取游标

sql1 = '''
    insert into company(id, name, age, address, salary)
    values(1, "lisi", 19, "成都", 8000);
'''

sql2 = '''
    insert into company(id, name, age, address, salary)
    values(2, "lisan", 20, "成都", 9000);
'''
# c.execute(sql1)  # 执行sql语句
# conn.commit()   # 提交数据库操作语句
c.execute(sql2)  # 执行sql语句
conn.commit()   # 提交数据库操作语句
conn.close()    # 关闭数据库
print("成功插入数据表")
"""
# 查询数据
conn = sqlite3.connect("test.db")  # 打开或创建数据库
print("Open database successful")
c = conn.cursor()   # 获取游标

sql2 = "select id, name, age, address, salary from company"
cursor = c.execute(sql2)

for row in cursor:
    print('id = ', row[0])
    print('name = ', row[1])
    print('age = ', row[2])
    print('address = ', row[3])
    print('salary = ', row[4], "\n")

conn.close()    # 关闭数据库
print("查询完毕")

# sqlite3.OperationalError: database is locked：需关闭数据库链接，再执行程序，sqllist是单线程数据库不支持多用户写
# sqlite3.OperationalError: near "id": syntax error：sql语句错误
