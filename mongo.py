from pymongo import MongoClient
client = MongoClient()
db = client.inventory
col = db.inventory
col.insert_one({"Created":"Yes"})
client.close()
