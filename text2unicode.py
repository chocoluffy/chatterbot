# -*- coding: utf-8 -*-
import json 

file = 'conversation.json' # human readable
newfile = 'conversation_unicode.json' # for chatbot, unicode file


with open(file) as json_data:
    d = json.load(json_data)
    # string = json.dumps(d, encoding='utf8')
    with open(newfile, 'w') as outfile:
    	json.dump(d, outfile)