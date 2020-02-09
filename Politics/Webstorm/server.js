//Load the HTTP Module
// var http = require("http");
//
// // Create HTTP server and listen on port 8000 for requests
// http.createServer(function(request, response){
//
//   // set the response HTTP header with HTTP status and Content type
//   response.writeHead(200, {'Content-Type': 'text/plain'});
//
//   //Send the response body "Hello World"
//   response.end('Hello World\n');
// }).listen(8000);
//
//
// //Print URL for accessing server
// console.log('Server running at http://127.0.0.1:8000/');

var express = require('express');
var app = express();
var square = require('./square');

app.get ('/', function(req, res){
  res.send('Hello world!');
});

app.listen(3000, function(){
  console.log('Example app listening on port 3000');

});

console.log('the area of a square with a width of 4 is ' + square.area(4));

setTimeout(function () {
  console.log('First');
}, 3000);
console.log('Second');

console.log(parseInt('0x10'));
