# interacts with mongodb - database name - newdb, collection name - users

from pymongo import MongoClient
client = MongoClient("mongodb+srv://jaideep:nilesh6@cluster0.st5bm.mongodb.net/demo?retryWrites=true&w=majority")
db = client.get_database('newdb')
records = db.users
a = records.count_documents({})

print(a)

def temp1(fname, mname, lname):
    document1 = {
            #"name":fname+'&nbsp'+mname+'&nbsp'+lname ,
            "name": fname + " " + mname + " " + lname,
            "id":fname[0:1]+lname,
            "role":"To be defined",
            "password":"1234"
            }

    records.insert_one(document1)
    id1 = (records.find_one({"name": fname + " " + mname + " " + lname}))["id"]
    #print(id1)
    return (id1)


# takes id from app.py
def temp2(s):
    try:
        name = (records.find_one({"id": s}))["name"]
        role = (records.find_one({"id": s}))["role"]

    except Exception as e:
        print(e)
        return ('New User','NOC and SOC team')

#returns name and role based on id
    return (name,role)

def temp3(userid, password):

    try:
        userid = (records.find_one({"id": userid}))["id"]
        #password = (records.find_one({"password": password}))["password"]

    except Exception as e:
        print(e)
        useridresp = "User id do not exist"
        passwordresp = "Not checked"
        name = "dummy"
        #return ('Userid do not exist','Wrong Password')
        return (useridresp, passwordresp,name)

    try:
        #userid = (records.find_one({"id": userid}))["id"]
        password = (records.find_one({"password": password}))["password"]

    except Exception as e:
        print(e)
        useridresp = "Passed"
        passwordresp = "Password do not match"
        name = "dummy"
        return (useridresp, passwordresp,name)

    name = (records.find_one({"id": userid}))["name"]
    useridresp = "Passed"
    passwordresp = "Passed"

    return (useridresp, passwordresp,name)
