import urllib.request
import urllib.parse
import string

def get_params():
    url = "http://www.baidu.com/s?"
    params = {
        "wd":"中文",
        "key":"zhang",
        "value":"san"
    }
    str_params = urllib.parse.urlencode(params)  #wd=%E4%B8%AD%E6%96%87&key=zhang&value=san
    print(str_params)
    final_url = url + str_params
    end_url = urllib.parse.quote(final_url,safe=string.printable)
    print(end_url)
    response = urllib.request.urlopen(final_url)
    data = response.read().decode("utf-8")
   # print(data)

get_params()