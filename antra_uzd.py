import pymongo
import json
from pymongo import MongoClient, InsertOne
from pymongo.server_api import ServerApi

# 1 Sukurkite restoranų duomenų rinkinį (pridedamas zip failas)

client = MongoClient('localhost', 27017)
db = client['myDatabase']
collection = db['restaurants']
file_data = []

with open(r"retaurants.json") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        file_data.append(InsertOne(myDict))
               
collection.bulk_write(file_data)

# 2 Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio

uzklausa2 = collection.find()
# for match in uzklausa2:
    # print(match)
    
    
# for x in collection.find():
  # print(x)

# 3 Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams

uzklausa3 = collection.find({},{ "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1 })
# for match in uzklausa3:
    # print(match)
    
    
# for x in collection.find({},{ "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1 }):
  # print(x)

# 4 Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko field_id visiems dokumentams

uzklausa4 = collection.find({},{ "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 0 })
# for match in uzklausa4:
    # print(match)
    
    
# for x in collection.find({},{ "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 0 }):
  # print(x)

# 5 Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus

uzklausa5 = collection.find({"borough": "Bronx"},{})
# for match in uzklausa5:
    # print(match)
    
    
# for x in collection.find({"borough": "Bronx"},{}):
  # print(x)

# 6 Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100 (duomenis gali reikėti agreguoti).

uzklausa6 = collection.aggregate([{"$match": {"$expr": {"$and": [{"$gte": [{"$sum": "$grades.score"}, 80]}, {"$lte": [{"$sum": "$grades.score"}, 100]}]}}}],{})
# for match in uzklausa6:
    # print(match)
    
    
# for x in collection.aggregate([{"$match": {"$expr": {"$and": [{"$gte": [{"$sum": "$grades.score"}, 80]}, {"$lte": [{"$sum": "$grades.score"}, 100]}]}}}],{}): #"grades.score": { "$gt": 79} },{}):
    # print(x)
  
# 7 Parašykite užklausą, kad cuisine būtų išdėstyta didėjimo tvarka, o borough - mažėjimo.

uzklausa7 = collection.find().sort([("cuisine", 1), ("borough", -1)])
# for match in uzklausa7:
    # print(match)
    
    
# for x in collection.find().sort([("cuisine", 1), ("borough", -1)]):
  # print(x)

client.close()