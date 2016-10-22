# -*- coding: utf-8 -*-
import json 

file = 'backupclean161021.json' # human readable
newfile = 'newdata161021.json' # for chatbot, unicode file


with open(file) as json_data:
    d = json.load(json_data)
    # string = json.dumps(d, encoding='utf8')
    with open('newdata161021.json', 'w') as outfile:
    	json.dump(d, outfile)