from pymongo import MongoClient

client = MongoClient()

# database
db = client["test-db"]

# table
people = db["People"]

match1 = people.find_one({"first_name": "Mahmood"})
print("find_one result:")
print(match1)

print("find result:")
matches2 = people.find({"first_name": "Mahmood"})
for match2 in matches2:
    print(match2)
