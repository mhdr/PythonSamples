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
people=db["People"]

new_people=[]

print("Starting loop : {0}".format(time.asctime( time.localtime(time.time()) )))

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
    new_people.append(new_person)

print("End of loop : {0}".format(time.asctime( time.localtime(time.time()) )))

print("Starting insert : {0}".format(time.asctime( time.localtime(time.time()) )))
ids=people.insert(new_people)
print("End of insert : {0}".format(time.asctime( time.localtime(time.time()) )))