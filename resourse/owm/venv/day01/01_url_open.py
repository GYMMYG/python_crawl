import urllib.request

def load_data():
    url = "http://www.baidu.com/"
    #get请求
    #http请求
    #response :http响应对象
    response = urllib.request.urlopen(url)
    print(response)
    #读取内容
    data = response.read()  #为byte类型
    print(data)
    #将文件获取内容转换成字符串
    str_data = data.decode("utf-8")
    print(str_data)
    #将数据写入文件
    with open("baidu.html","w",encoding="utf-8") as f:
        f.write(str_data)
    #将字符串类型转换成bytes
    str_name = "baidu"
    byte_str = str_name.encode("utf-8")
    print(byte_str)
    #python爬取的类型：str  bytes  需要编码或解码

load_data()