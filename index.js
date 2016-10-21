var express = require('express');
var bodyParser = require('body-parser');
var request = require('request');
var app     = express();



//Note that in version 4 of express, express.bodyParser() was
//deprecated in favor of a separate 'body-parser' module.
app.use(bodyParser.urlencoded({ extended: true })); 

app.post('/chat', function(req, res) {
	var query = req.body.query || "";
	var auth = req.body.auth || "";

	request({ 
		url: 'http://localhost:5002/chat',
		method: 'POST',
		json: {'query': query, 'auth': auth}
		}, function (error, response, body) {
			res.send(body);
		}
	);
});

app.listen(5003, function() {
  console.log('Server running at http://127.0.0.1:5003/');
});