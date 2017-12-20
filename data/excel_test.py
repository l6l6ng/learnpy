import xlwings as xw

app = xw.apps.active

wb = xw.books.active
wb = app.books.active

sht = xw.sheets.active
sht = wb.sheets.active

print(sht.Range('A1'))
