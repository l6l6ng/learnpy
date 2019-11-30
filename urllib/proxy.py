import urllib.request

url = 'http://tieba.baidu.com'

header = {
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

proxy_handler = urllib.request.ProxyHandler({
    'http': 'web-proxy.oa.com:8080',
    'https': 'web-proxy.oa.com:8080'
})

opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

request = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))