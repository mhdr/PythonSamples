from pymongo import MongoClient

client=MongoClient()

print(client.database_names())

# database
db=client["test-db"]

print(db.collection_names())

# table
people=db["People"]