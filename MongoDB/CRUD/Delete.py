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

print(people.count())

people.remove({"_id":id2})

print(people.count())