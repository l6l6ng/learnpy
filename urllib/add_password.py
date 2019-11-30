import urllib.request

url = 'http://tieba.baidu.com'
user = 'user'
password = 'password'
pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None, url, user, password)

auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)
opener = urllib.request.build_opener(auth_handler)
responese = opener.open(url)
print(responese.read().decode('utf-8'))