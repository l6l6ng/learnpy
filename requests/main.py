import json
import requests as rq
from requests import exceptions

Url = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([Url,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_methons():
    response = rq.get(build_uri('users/dfsd534'))
    print(better_print(response.text))

def params_request():
    response = rq.get(build_uri('users'),params={'since':11})
    # print(better_print(response.text))
    print(response.request.headers)
    print(response.url)

def timeout_request():
    try:
        response = rq.get(build_uri('user/email'),timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        print(response.text)
        print(response.status_code)


def json_request():
    response = rq.patch(build_uri('user'),auth=('dfsd534','123456'),json={'name':'123456'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

def hard_request():
    from requests import Request,session
    s = session()
    headers = {'User-Agent':'fake1.3.4'}
    req = Request('GET',build_uri('user/emails'),auth=('dfsd534','123456'),headers=headers)
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)

    resp = s.send(prepped,timeout=5)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)

if __name__ == '__main__':
    # request_methons()
    # params_request()
    #json_request()
    #timeout_request()
    hard_request()