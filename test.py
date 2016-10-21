# -*- coding: utf-8 -*-
from chatterbot import ChatBot

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
    database='chattbot',
    database_uri='mongodb://adatech:adaseikou@ds019916.mlab.com:19916/chattbot'
)

while True:
	query = input("ask: ")
	print(str(chatbot.get_response(query)))
	print('')
