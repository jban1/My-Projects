from pymongo import MongoClient
client = MongoClient("mongodb+srv://jaideep:nilesh6@cluster0.st5bm.mongodb.net/newdb?retryWrites=true&w=majority")
db = client.get_database('newdb')
records = db.collection
a = records.count_documents({})
print(a)

new_record = {
    "age":"56",
    "sex":"male"
            }

new_record_1 = [
    {
    "age":"56",
    "sex":"male"
            },
            {
    "age":"62",
    "sex":"xxmale"
            }
]
#records.insert_one(new_record)
#records.insert_many(new_record_1)

b = records.count_documents({})
print(b)

print(list(records.find()))

print (records.find_one({"age": "56"}))

record_modify = {"sex": "updated"}

records.update_many({"age": "56"}, {"$set":record_modify})

#records.delete_one({"age":"56"})
