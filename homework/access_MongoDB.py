"""
Use Python to access MongoDB
"""
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['test']
collection = db['member']

mydata = {"name":"Kevin", "phone":"0912345678","email":"test@abc.com"}
result = collection.insert_one(mydata)
print("result.inserted_id: ", result.inserted_id)

mydata_list = [
    {"name":"Kevin2", "phone":"0912345678","email":"test2@abc.com"},
    {"name":"Kevin3", "phone":"0912345678","email":"test3@abc.com"},
    {"name":"Kevin4", "phone":"0912345678","email":"test4@abc.com"}
]
result = collection.insert_many(mydata_list)
print("result.inserted_ids: ", result.inserted_ids)

cnt = collection.count_documents({})
print("cnt: ", cnt)
collection.delete_one({})
cnt = collection.count_documents({})
print("cnt: ", cnt)
collection.delete_one({"name":"Kevin4"})
cnt = collection.count_documents({})
print("cnt: ", cnt)

result = collection.delete_many({"name":"Kevin"})
print("result.deleted_count: ", result.deleted_count)

collection.update_one({"name":"Kevin3"}, {"$set": {"name":"Peter"}})

collection.update_many({"name":"Kevin"}, {"$set": {"name":"Peter"}})

print("collection.find_one()")
result = collection.find_one()
print(result)

print("collection.find()")
result = collection.find()
for x in result:
    print(x)

print("collection.find().sort()")
result = collection.find().sort("age",-1)
for x in result:
    print(x)

print("collection.find().limit()")
result = collection.find().limit(2)
for x in result:
    print(x)

