## Usage

`pm2 start index.js --max-memory-restart 150M`
`python3 app.py` makes sure the backend runs in here: http://localhost:5002/chat

Important fact that chatterbot must be installed under python3. Thus, in order to deploy on Ubuntu server, we must create an virtual environment that have python3 support.

(create a virtualenv using conda)[https://www.continuum.io/blog/developer-blog/python-3-support-anaconda]

`conda create -n py3k python=3`

which probably means need to install flask under python3 environment with `sudo pip3 install Flask-API`

## Trouble Shooting

- install dependencies

After listing all version info, pip3 seems to install chatterbot into `/usr/local/lib/python3.4/dist-packages` with `sudo pip3 install chatterbot` while, we are using `python3.5` version.

`python3.5 -m pip install chatterbot` is the correct way to accomplish this goal.

Besides, we also need to install the followings: `python3.5 -m pip install flask` and `python3.5 -m pip install Flask-API`.

`sudo pip3 install python-levenshtein` to install this extension.

- wechat compatibility

sometimes, if a messege is not responded fast enough, it will resend the msg and if not finally, it will just responds with "不提供服务"


## Update UTzhushou

First test on planB, then manually copy modified files to AirLoftTech to push to UTzhushou.

## Important Notes

`newdata...json` file mainly used as the real database material.

`backupclean...json` file mainly used as a cleaner view of material.

Try to format things in backupclean(more human readable), then use `jsondump.py` to convert it into unicode file.(16.10.21: upload all latest json object to mongolab database).

Then, try locally test the chatbot with `test.py`.

I re-structure the files into different folders, the files inside `secondary` are less important than the first-level files.

`text2unicode.py` simply just load the json file and restore it into another file, but can help convert text into unicode, which python3 can consume, making sure `python3 test.py` can run is the key!!

`conversation.json` contains usual sentences, which will be hard-coded for chatbot, can be shared with Google Docs and extended it by all. It requires no machine learning, simply hard match! Used by `text2unicode.py`, by adding most frequent fix response to this json, and run that script, the produced `conversation_unicode.json` can be used in production.

`conversation_unicode.json`, the file generated after running `text2unicode.py`, is used by `app.py` and `test.py`.

`json2mongo.py` uploads json file to mongolab, with same format as chatterbot examples!



## Reading Materials

- [mongolab uri](http://stackoverflow.com/questions/32679227/remote-mongo-connection-via-pymongo)
- [pymongo insert a document into collection](https://docs.mongodb.com/getting-started/python/insert/)