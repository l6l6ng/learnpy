import requests as rq

# def get_key_info(response,*args, **kwargs):
#
#     print(response.headers['Content-Type'])
#
# def main():
#     rq.get('https://www.baidu.com',hooks=dict(response=get_key_info))
#
# main()

def get_key_info(response,*args,**kwargs):
    print(response.headers['Content-Type'])

def main():
    rq.get('https://api.github.com',hooks=dict(response=get_key_info))

main()