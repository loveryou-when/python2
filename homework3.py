import urllib.request
url ='http://www.tiaomao.com'
proxy_handle = {
    'http':'1.198.73.198:9999',
    'http':'183.51.190.51:33913'
}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf8'))
if response.status != 200:
    print('%S 爬取失败'%url)
else:
    print(response.status)
