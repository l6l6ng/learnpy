import urllib.request

url = 'https://tieba.baidu.com'

headers = {}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))