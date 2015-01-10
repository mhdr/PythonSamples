from pymongo import MongoClient
from Person import Person

client=MongoClient()

# drop last db
client.drop_database("test-db")

# database
db=client["test-db"]

# table
people=db["People"]

new_person1=Person.initialize("Mahmood","Ramzani",1985,5,22)

new_person2=Person.initialize("Javad","Najafi",1984,7,15)

new_person3=Person.initialize("Mahmood","Rohani",1985,3,11)


id1= people.insert(new_person1.dic())
id2= people.insert(new_person2.dic())
id3= people.insert(new_person3.dic())

print(id1)
print(id2)
print(id3)