# -*- coding: utf-8 -*-
import json
from pprint import pprint

with open('database.json') as data_file:    
    data = json.load(data_file)
    res = {
        'data': []
    }
    print('{ "data": [')
    # print(len(data.keys()))
    for text in data.keys():
    	if data[text]['in_response_to']:
    		# print text, " Ans: ", data[text]['in_response_to'][0]['text'], ' importance: ', data[text]['in_response_to'][0]['occurrence']
            question = text
            answer = data[text]['in_response_to'][0]['text']
            occurrence = data[text]['in_response_to'][0]['occurrence']
            obj = {
    			'question': question,
    			'answer': answer,
    			'frequency': occurrence
    		}
            print(obj, ',')
            res['data'].append(obj)
    print(']}')

# pprint(data)