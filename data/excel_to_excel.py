#coding=utf-8
import xlwings as xw
import pandas as pd

app = xw.App(visible=False,add_book=True)
app.display_alerts = False
app.screen_updating = False

filepath = r'./excel.xlsx'

wb = app.books.open(filepath)
sht1 = wb.sheets['sheet1']
data1 = sht1.range('A1').expand().value
# sht2 = xw.sheets.add(name='sheet2')
sht2 = wb.sheets['sheet2']
# rng2 = sht2.range('A1').expand().value
sht2.value = data1

# data2 = [[0]*6 for i in range(300)]
# print data2
data2 = dict()

for i in range(0,1050):
    if (int(data1[i][1]) in data2):
        if int(data1[i][4]) == 1:
            data2[data1[i][1]][6] = data1[i][3]

        if data2[data1[i][1]][3] == '':
            data2[data1[i][1]][3] = data1[i][3]
        elif data2[data1[i][1]][4] == '':
            data2[data1[i][1]][4] = data1[i][3]
        elif  data2[data1[i][1]][5] == '':
            data2[data1[i][1]][5] = data1[i][3]
    else:
        data2.update({int(data1[i][1]):{0:int(data1[i][0]),1:data1[i][2],2:data1[i][3],3:'',4:'',5:'',6:''}})
        if int(data1[i][4]) == 1:
            data2[data1[i][1]][6] = data1[i][3]

# print list(data2['1159'])
# sht2.range('A1').options(expand='table').value = data2
# print data2
ls = [[0 for j in range(7)] for i in range(300)]

m = 0;
for (d,x) in data2.items():
    ls[m][0] = x[0]
    ls[m][1] = x[1]
    ls[m][2] = x[2]
    ls[m][3] = x[3]
    ls[m][4] = x[4]
    ls[m][5] = x[5]
    ls[m][6] = x[6]
    m = m + 1

# sht2.range('A1').options(expand='table').value = ls
sht2.range('A1').value = 2
wb.save()
wb.close()
app.quit()


