//this is the server side js
//import express.js
var express = require('express');
//assign it to variable app
var app = express();
//create a server and pass in app as a request handler
var serv = require('http').Server(app); //Server-11

//send a index.html file when a get request is fired to the given
//route, which is ‘/’ in this case
app.get('/',function(req, res) {
	res.sendFile(__dirname + '/build/index.html');
});
//this means when a get request is made to ‘/client’, put all the
//static files inside the client folder
// Under ‘/client’. See for more details below

app.use(express.static(__dirname + '/build'));

//listen on port 2000
serv.listen(process.env.PORT || 11155, "0.0.0.0");
console.log("Server started.");
