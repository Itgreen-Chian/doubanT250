import xlwt


# wordbook = xlwt.Workbook(encoding="utf-8")   # 创建workbook对象
# wordsheet = wordbook.add_sheet("sheet1")   # 创建一页表格
# wordsheet.write(0, 0, "book")   # 写入数据
# wordbook.save("12.xls")   # 保存文件

wordbook = xlwt.Workbook(encoding="utf-8")
wordsheet = wordbook.add_sheet("sheet1")   # 创建一页表格
for i in range(0, 9):
    for j in range(0, i+1):
        wordsheet.write(i, j, "%d * %d = %d" % (i+1, j+1, (i+1)*(j+1)))

wordbook.save("student.xls")   # 保存文件