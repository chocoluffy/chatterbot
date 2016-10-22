# -*- coding: utf-8 -*-
# using pymongo to insert all json fragment into mongolab db.
from pymongo import MongoClient
from datetime import datetime
import json 

file = 'backupclean161021.json' # human readable
conversation = 'conversation.json' # hard-coded conversation materials
uri = 'mongodb://adatech:adaseikou@ds019916.mlab.com:19916/chattbot'
client = MongoClient(uri)
db = client.chattbot

# example json object, to test mongolab connection.
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

# open backup json file.
with open(file) as json_data:
    d = json.load(json_data)
    for key in d:
		result = db.statements.insert_one(
		    {
		        "text": key,
		        "in_response_to": d[key]['in_response_to']
		    }
		)

