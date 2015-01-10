# http://docs.mongodb.org/manual/reference/operator/update/

from pymongo import MongoClient

client=MongoClient()

# drop last db
client.drop_database("test-db")

# database
db=client["test-db"]

# table
people=db["People"]

new_person1={"FirstName" : "Mahmood",
            "LastName" : "Ramzani",
            "Gender": "Male",
            "BirthDate" : {"Year" : 1985 , "Month" : 5 , "Day" : 22}}

new_person2={"FirstName" : "Javad",
            "LastName" : "Najafi",
            "Gender": "Male",
            "BirthDate" : {"Year" : 1984 , "Month" : 7 , "Day" : 13}}

new_person3={"FirstName" : "Mahmood",
            "LastName" : "Rohani",
            "Gender": "Male",
            "BirthDate" : {"Year" : 1985 , "Month" : 8 , "Day" : 8}}


id1= people.insert(new_person1)
id2= people.insert(new_person2)
id3= people.insert(new_person3)

match1=people.find_one(id1)
match1["LastName"]="Ramzani Sesemasi"

# Upsert parameter will insert instead of updating if the post is not found in the database
people.update({"_id":id1},{"$set":match1},upsert=False)

match2=people.find_one({"LastName":"Ramzani Sesemasi"})
print(match2)