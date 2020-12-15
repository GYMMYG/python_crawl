from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import pymysql
import csv
engine = create_engine("mysql+pymysql://BGC_stu:Bigdatacourse123@202.117.45.244:33306/bgd_course?charset=utf8", echo=True)
Base = declarative_base()


# 定义Course对象，课程表对象
class Course(Base):
    # 表的名字
    __tablename__ = '2183211376_郭英明_table02'
    id = Column(Integer, primary_key=True)
    col1 = Column(Integer, default=None, nullable=False, comment='col1')
    col2 = Column(String(200), default=None, nullable=False, comment='col2')
    col3 = Column(String(200), default=None, nullable=False, comment='col3')
    col4 = Column(String(200), default=None, nullable=False, comment='col4')
    col5 = Column(String(200), default=None, nullable=False, comment='col5')
    col6 = Column(String(200), default=None, nullable=False, comment='col6')
    col7 = Column(String(200), default=None, nullable=False, comment='col7')
    col8 = Column(String(200), default=None, nullable=False, comment='col8')

Base.metadata.create_all(engine)  #创建表结构 （这里是父类调子类）

from sqlalchemy.orm import sessionmaker

# 创建session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

with open(r'D:\桌面\basic_info.csv', 'r', encoding='utf-8')as csvfile:
    data = csv.reader(csvfile)
    for index, rows in enumerate(data):
        course = Course(id=index+1,col1=rows[0],col2=rows[1],col3=rows[2],col4=rows[3],col5=rows[4],col6=rows[5],col7=rows[6],col8=rows[7])
        # course.id = index + 1
        # course.col1,course.col2,course.col3,course.col4,course.col5,course.col6,course.col7,course.col8 = rows
        session.add(course)
        session.commit()
