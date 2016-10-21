# -*- coding: utf-8 -*-
# using pymongo to insert all json fragment into mongolab db.
from pymongo import MongoClient
from datetime import datetime
import json 

file = 'backupclean161021.json' # human readable
uri = 'mongodb://adatech:adaseikou@ds019916.mlab.com:19916/chattbot'
client = MongoClient(uri)
db = client.chattbot

# open backup json file.
with open(file) as json_data:
    d = json.load(json_data)
    example = {
    	"唱个小曲儿来听听": {
			"in_response_to": [
				{
					"occurrence": 1,
					"text": "喵喵喵？"
				}
			]
		}
    }
    for key in example:
		result = db.statements.insert_one(
		    {
		        "text": key,
		        key: example[key]
		    }
		)

