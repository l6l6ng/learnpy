import urllib.request
import urllib.error

url = "http://www.google.com"
try:
    response = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print('code:' + e.code + '\n')
    print('reason:' + e.reason + '\n')
    print('headers:' + e.headers + '\n')