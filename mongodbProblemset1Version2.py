#-------------------------------------------------------------------------------
# Name:        MongoDb creating the database within the script itself.
# Purpose: Education
#
# Author:      mmk
#
# Created:     21/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriasoft>
#-------------------------------------------------------------------------------
import pymongo
from bson.json_util import dumps

#Connecting to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Connecting to the database...
medium_db=client["MediumDatabase2"]


#Connecting to the exact collection we need
my_collection=medium_db["Medium1"]
#check if there is collection exist
collist = medium_db.list_collection_names()
if "Medium1" in collist:
     pass
#insert the fields..
else:
    my_entries=[
          { "_id": 1,"MediumUserName": "mmk","UserNumberOfPost": 40,"PostLength": 300  },
         { "_id": 2,"MediumUserName": "gloria","UserNumberOfPost": 100,"PostLength": 5000 },
         {"_id": 3,"MediumUserName": "fela","UserNumberOfPost": 250,"PostLength": 500},
         {"_id": 4,"MediumUserName": "zokky","UserNumberOfPost": 450,"PostLength": 5000},
         { "_id": 5,"MediumUserName": "nonso","UserNumberOfPost": 450, "PostLength": 800 }

         ]

    my_collection.insert_many(my_entries)





#print list of the _id values of the inserted documents:


#===============================================================================
#FUNCTION  TO  COUNT NUMBER OF ENTRIES IN THE COLLECTION
#===============================================================================

def num_entries():
    '''Function to determined number of entries'''
     #function to count number of entries in the collection
    entries=my_collection.find()
    num_of_entries= entries.count()

    print("The number of documents in my collection:", num_of_entries )


#===============================================================================
#FUNCTION  TO  count of all entries with a field matching a given string of your choosing.
#===============================================================================

def query_entries(field_name,pattern_to_match):
     '''FUNCTION  TO  count of all entries with a field matching a given string of your choosing'''

    #print(my_collection.find({"EmployeeName" : "Smith"}).count())
     print(" All entries with number of post 450 in field ‘UserNumberOfPost’: ",my_collection.find({field_name: pattern_to_match}).count())


#===============================================================================
#FUNCTION  TO    PRINTS ALL ENTRIES AS PRETTY-PRINTED JSON
#===============================================================================
def pprint_json():
    ''' FUNCTION  TO    PRINTS ALL ENTRIES AS PRETTY-PRINTED JSON'''

     # create a empty dictionary

    # convert into JSON:
    for coll in my_collection.find() :
            print (dumps(coll,indent=4))


def main():
    #pass
    print("************************************************************")
    num_entries()
    print("************************************************************")

    #print()
    field_name="UserNumberOfPost"
    pattern_to_match=450
    print("************************************************************")
    query_entries(field_name,pattern_to_match)
    print("************************************************************")

    pprint_json()


if __name__ == '__main__':
    main()
