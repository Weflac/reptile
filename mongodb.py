# -*- coding:utf-8 -*-

from pymongo import MongoClient


client = MongoClient('localhost', 27017)

url = 'http://www.baidu.com/'
html = '..'
db = client.nuoxiao
collection = db.webpage

# db.webpage.insert({'url': url, 'html': html})
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

# result = collection.insert(student)
# print(result)

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# result = collection.insert([student1,student2])
# print(result)

results = collection.find({'age': {'$gt': 20}})
print(results)
