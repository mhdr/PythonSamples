__author__ = 'mahmood'

from pymongo import MongoClient

client=MongoClient()

# drop last db
client.drop_database("test-db")

# database
db=client["test-db"]

# table
people=db["People"]

new_people=[]

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

new_people.append(new_person1)
new_people.append(new_person2)
new_people.append(new_person3)

ids=people.insert(new_people)

for id in ids :
    print(id)