from pymongo import MongoClient
import pandas as pd
import pymongo
conn = MongoClient('localhost', 27017)
db = conn["Project"]
col = db["rating"]

#df= col.find_one()
#df = pd.DataFrame(list(col.find()))
#df = df.drop(['_id'], axis = 1)
#print(df)

def update_rating(dit):
    for i in dit:
        filter=({"$and":[{"userId":1},{"movieId":i}]})
        newval={"$set":{"rating":dit[i]}}
        col.update_one(filter, newval)

    
