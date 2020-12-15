import urllib.request

def handler_openner():
    #the "urlopen" system doesn't have the function of adding "handler",we need  to define it by ourselves
    #urllib.request.urlopen()
    #http:80  https:443
    #urlopen能够请求数据因为有自己的handler和opener
    url = "https://www.baidu.com/"
    handler = urllib.request.HTTPHandler()   #HTTPHandler 一种handler的类型
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    print(response)
    print(response.read().decode("utf-8"))

handler_openner()