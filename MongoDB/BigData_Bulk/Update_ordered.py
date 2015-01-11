# http://api.mongodb.org/python/current/examples/bulk.html
__author__ = 'Mahmood'

import time
from pymongo import MongoClient
from bson.objectid import ObjectId

client=MongoClient()

# drop last db
client.drop_database("test-db")

# database
db=client["test-db"]

# table
people_bulk=db["People"].initialize_ordered_bulk_op()
people=db["People"]

print("Starting insert loop : {0}".format(time.asctime( time.localtime(time.time()) )))

for i in range(1,100000):
    new_person={"FirstName" : "Mahmood",
            "LastName" : "Ramzani",
            "Gender": "Male",
            "BirthDate":{"Year":1985,"Month":5,"Day":22},
            "Country":"Iran",
            "City":"Rasht",
            "email":"mahmoodramzani@gmail.com",
            "user_name":"mahmoodramzani",
            "password":"1234"}

    ids=people_bulk.insert(new_person)

print("End of insert loop : {0}".format(time.asctime( time.localtime(time.time()) )))

print("Starting execute : {0}".format(time.asctime( time.localtime(time.time()) )))
people_bulk.execute()
print("End of execute : {0}".format(time.asctime( time.localtime(time.time()) )))

matches=people.find()
# initialize again because you can run execute command once
people_bulk=db["People"].initialize_ordered_bulk_op()

print("Starting update loop: {0}".format(time.asctime( time.localtime(time.time()) )))
for match in matches:
    match["LastName"]="Ramzani Sesemasi"
    id=match["_id"]
    people_bulk.find({"_id":id}).update({"$set":match})

print("End of update loop: {0}".format(time.asctime( time.localtime(time.time()) )))

print("Starting execute : {0}".format(time.asctime( time.localtime(time.time()) )))
people_bulk.execute()
print("End of execute : {0}".format(time.asctime( time.localtime(time.time()) )))