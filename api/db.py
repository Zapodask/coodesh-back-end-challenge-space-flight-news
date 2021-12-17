from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://zapodask:zapodask@spacecluster.kngaq.mongodb.net/spacedb?retryWrites=true&w=majority"
)

db = client["spacedb"]
