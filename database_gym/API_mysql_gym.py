from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import requests
import json
import os
import time
import pymysql
import csv


#api调用
class Crawl:

    def __init__(self, url):
        self.url = url

    def get_data(self):
        r = requests.get(self.url)
        content = json.loads(r.text)
        return content

def get_data(url):
    s = Crawl(url)
    content = s.get_data()
    return content

id1 = 12784279
key = 'DKVGy8lY'
url = 'https://v0.yiketianqi.com/api?version=v9&appid=%d&appsecret=%s'%(id1,key)
json_data = get_data(url)

#写入文件
item = json.dumps(json_data)
with open('weather.json', "w", encoding='utf-8') as f:
    f.write(item + ",\n")

datas = json_data['data']
# print(type(datas))
# print(type(datas[0]))

#入库
engine = create_engine("mysql+pymysql://BGC_stu:Bigdatacourse123@202.117.45.244:33306/bgd_course?charset=utf8", echo=True)
Base = declarative_base()

# 定义shares对象，课程表对象
class Weather(Base):
    # 表的名字
    __tablename__ = 'Homework4_2183211376_郭英明_weather_xian'
    id = Column(Integer, primary_key=True)
    day = Column(String(200), default=None, nullable=False, comment='day')
    date = Column(String(200), default=None, nullable=False, comment='date')
    wea = Column(String(200), default=None, nullable=False, comment='wea')
    tem = Column(String(200), default=None, nullable=False, comment='tem')
    tem1 = Column(String(200), default=None, nullable=False)
    tem2 = Column(String(200), default=None, nullable=False)
    sunrise = Column(String(200), default=None, nullable=False)
    sunset = Column(String(200), default=None, nullable=False)

Base.metadata.create_all(engine)  #创建表结构 （这里是父类调子类）

from sqlalchemy.orm import sessionmaker

# 创建session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

count = 1
for data in datas:
    weat = Weather()
    weat.id = count
    count += 1
    weat.day = data['day']
    weat.date = data['date']
    weat.wea = data['wea']
    weat.tem = data['tem']
    weat.tem1 = data['tem1']
    weat.tem2 = data['tem2']
    weat.sunrise = data['sunrise']
    weat.sunset = data['sunset']
    session.add(weat)
    session.commit()