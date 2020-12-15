import pymongo
import csv

#连接的用户如果是在特定数据库，而非admin数据库，需要指定认证的源数据库
uri = "mongodb://BGC_stu:Bigdatacourse123$@202.117.45.244:27017/?authSource=bdg_course"
client = pymongo.MongoClient(uri)
db = client.bdg_course
print("Database created........")
col1 = db['2183211376_郭英明_collection01']

with open(r'D:\桌面\quotes.csv', 'r', encoding='gb18030')as csvfile:
    # 调用csv中的DictReader函数直接获取数据为字典形式
    reader = csv.DictReader(csvfile)
    for each in reader:
        col1.insert_one(each)
        # print(each)

