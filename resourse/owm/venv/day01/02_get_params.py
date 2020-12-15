import urllib.request
import urllib.parse
import string


def get_method_params():
    #字符串拼接
    url = "http://www.baidu.com/s?wd="
    name = "加藤惠"
    final_url = url + name
    #将包含汉字的网址进行转义
    encode_new_url = urllib.parse.quote(final_url,safe = string.printable)
    #print(final_url)
    #使用代码发送网络请求
    #网址里面包含了中文报错；需要url转义
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    #UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-12: ordinal not in range(128)
    #python是解释性的语言，只支持ascii，不支持中文
    data = response.read().decode()
    print(data)
    with open("hui.html","w",encoding="utf-8") as f:
        f.write(data)

get_method_params()