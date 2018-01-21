import requests as rq
# r = rq.get('http://www.baidu.com')
# print(r)
# r1 = rq.post('http://httpin.org/post',data = {'key':'value'})
# print (r1)
# payload = {'key1':'value1','key2':'value2'}
# payload = {'key1':'value1','key2':['value2','value3']}
# r2 = rq.get("http://baidu.com",params=payload)
# print(r2.url)

r3 = rq.get('https://api.github.com/events')
# r3 = rq.get('https://www.baidu.com/events')
print(r3.text)

# print(r3.encoding)

# print(r3.content)

print(r3.json())
