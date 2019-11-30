import urllib.request
import  urllib.error

url = "http://tieba.baidu.com"

try:
    response = urllib.request.urlopen(url)
except urllib.error.URLError as e:
    print(e.reason)
