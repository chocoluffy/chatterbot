# -*- coding: utf-8 -*-
import json

result = {}
# open backup json file.
with open('experiment.json') as json_data:
    d = json.load(json_data)
    for key in d:
    	if len(d[key]['in_response_to']) > 0:
    		for res in d[key]['in_response_to']:
    			result[res['text']] = key
    with open('conversation.json', 'w') as outfile:
    	json.dump(result, outfile)