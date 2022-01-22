# interacts with mongodb - database name - newdb, collection name - users

from pymongo import MongoClient
client = MongoClient("mongodb+srv://jaideep:nilesh6@cluster0.st5bm.mongodb.net/demo?retryWrites=true&w=majority")
db = client.get_database('newdb')
records = db.users
a = records.count_documents({})

# takes id from app.py
def temp2(s):
    try:
        name = (records.find_one({"id": s}))["name"]
        role = (records.find_one({"id": s}))["role"]

    except Exception as e:
        print(e)
        return ('Anonymous User','with no role')

#returns name and role based on id
    return (name,role)
