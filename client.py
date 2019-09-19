import requests
import json

HEADERS = ""

def req(url, method, data={}):
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('Headers: %s' % HEADERS)

    if method == 'GET':
        return requests.get(url, headers=HEADERS)
    else:
        return requests.post(url, headers=HEADERS, data=data)

def toJSON(dic):
    return json.dumps(dic)

def toDic(txt):
    return json.loads(txt)

# test
response = req("https://httpbin.org/post", "POST", {"author":"kjm", "date":"20190919"})
body = response.text

resJson = toDic(body)
print(resJson)
print(resJson['form'])
