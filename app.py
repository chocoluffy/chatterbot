# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from flask.ext.api import FlaskAPI
from flask import request, current_app, abort, jsonify

chatbot = ChatBot(
    'Luffy',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    database="./newdata.json"
)
# chatbot.train("chatterbot.corpus.chinese")
app = FlaskAPI(__name__)

@app.route('/chat', methods=['POST'])
def chat():
	token = request.data.get('auth')
	if token == 'yushunzhe':
		query = request.data.get('query')
		# print(query)
		return {"response": str(chatbot.get_response(query))}
	else:
		return {"response": "wrong password."}

if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')
