import urllib.request


def load_data():
    url = "https://www.baidu.com/"  #有useragent时可以加s
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    #创建请求头信息
    request = urllib.request.Request(url,headers=header)
    # 动态添加headers信息
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    #请求网络数据
    #响应头
    response = urllib.request.urlopen(request)  #request包含url信息
    data = response.read().decode("utf-8")
    #获取完整url
    final_url = request.get_full_url()
    print(1,final_url)
   # print(response.headers)
    request_headers = request.headers
    print(request_headers)
    #打印特定信息  !!!!!!首字母大写，其他字母都要小写,不然返回none
    request_header = request.get_header("User-agent")
    print(request_header)
    with open("02_headers.html","w",encoding="utf-8") as f:
        f.write(data)

load_data()