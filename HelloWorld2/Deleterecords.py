# interacts with mongodb - database name - newdb, collection name - users

from pymongo import MongoClient
client = MongoClient("mongodb+srv://jaideep:nilesh6@cluster0.st5bm.mongodb.net/demo?retryWrites=true&w=majority")
db = client.get_database('newdb')
records = db.users
a = records.count_documents({})
#myquery = {"role": "To be defined"}
myquery = {"name": "dd"}

x = records.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

