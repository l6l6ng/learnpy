import requests as rq

def download_pic():
    '''
    下载图片
    '''

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    url = 'http://c.hiphotos.baidu.com/image/pic/item/7acb0a46f21fbe09810db97167600c338744ad00.jpg'

    response = rq.get(url,headers=headers,stream=True)

    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
    print(response.status_code)
    print(response.headers)
    print(response.content)

download_pic()
