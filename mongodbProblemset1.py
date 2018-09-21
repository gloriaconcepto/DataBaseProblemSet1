#-------------------------------------------------------------------------------
# Name:   MongoDB database problem
# Purpose:  Eduction
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
medium_db=client["MediumDatabase1"]

#Connecting to the exact collection we need
my_collection=medium_db["Medium"]


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
    my_dict = {}

    #iterate through the collection and add it to a dictionary
    for i ,v in enumerate(my_collection.find()):


         my_dict[i]=v

    # convert into JSON:

    parser = dumps(my_dict,indent=4)

    print(parser)








def main():
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
