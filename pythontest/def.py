import pymysql as pm
db = pm.connect('192.168.188.100','learnpy','123456','learnpy')
cursor = db.cursor()
cursor.execute('select * from test_2')

data = cursor.fetchone()
data = cursor.fetchall()
row = cursor.rowcount
count = cursor.rowcount
# data = cursor.fetchmany(3)
print(data)
print(row)
print(count)

for i in data:
    print(i)
db.close()