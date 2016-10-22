# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import json

### using local json file.
# chatbot = ChatBot(
#     'Luffy',
#     trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
#     database="./newdata161016.json"
# )

### using local db file.
# chatbot = ChatBot(
#     'Luffy',
#     trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
#     storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
#     logic_adapters=[
#         "chatterbot.adapters.logic.MathematicalEvaluation",
#         "chatterbot.adapters.logic.TimeLogicAdapter",
#         "chatterbot.adapters.logic.ClosestMatchAdapter"
#     ],
#     database="./newdata161021.json"
# )

### using mongolab uri.
chatbot = ChatBot(
    'Luffy',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter"
    ],
    database='chattbot',
    database_uri='mongodb://adatech:adaseikou@ds019916.mlab.com:19916/chattbot'
)


with open('conversation.json') as json_data: # if user-input text collide with hard-coded answers, responds back.
    d = json.load(json_data)
    while True:
    	query = input("ask: ")
    	if query in d.keys():
    		print(d[query])
    		print('')
    	else:
    		print(str(chatbot.get_response(query)))
    		print('')

















