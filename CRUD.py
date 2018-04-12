from pymongo import MongoClient
import pprint
client = MongoClient()
db            = client["new_db"]
collection    = db["my_collection"]

def insert():
    name = input("Enter Name:\t")
    age  = int(input("\nENter Age:\t"))
    enrn = int(input("\nENter enrollment num:\t"))

    collection.insert({
        "Name":   name,
        "Age" :   age,
        "Enroll": enrn
})
