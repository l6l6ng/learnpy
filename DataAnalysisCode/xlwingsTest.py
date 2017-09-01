import xlwings as xw

wb = xw.Book()
# wb = xw.Book('test.xlsx')
# wb = xw.Book(r'C:\path\to\file.xlsx')

sht = wb.sheets['sheet1']

sht.range("A1").value = 'foo 1'
a1 = sht.range('A1').value
sht.range('A1').value = [[1,2,3,4],[5,6,7,8]]
sht.range('A1').expand().value
