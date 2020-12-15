import  urllib.request

def creat_proxy_handler():
    url = "http://www.baidu.com/"

    #添加代理
    proxy = {
        #1.免费写法
        #"http":"http://120.77.249.46:8080"    #端口用：加在后面
        "http":"1"     #简化写法
        #2.付费  拼接账号密码
    }
    #多个代理时
    #proxy = [{},{}...]

    #代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    #创建opener
    opener = urllib.request.build_opener(proxy_handler)
    try:          #判断IP是否有效
        data = opener.open(url,timeout= 1).read().decode('utf-8')   #timeout 来判断是否超时
        # print(data)
        print("haha")
    except Exception as e:
        print(e)

creat_proxy_handler()