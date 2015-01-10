from pymongo import MongoClient

client=MongoClient()

# drop last db
client.drop_database("test-db")