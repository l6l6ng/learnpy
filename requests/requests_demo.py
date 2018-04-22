import requests as rq
params = {'a':1,'b':2}
response = rq.get('http://www.baidu.com',params)

print(response.headers)

print('>>>>>>')

print(response.text)

print('>>>status_code')

print(response.status_code)

print(response.reason)