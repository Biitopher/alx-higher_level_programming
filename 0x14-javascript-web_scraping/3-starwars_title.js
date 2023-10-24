#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  console.log(err || JSON.parse(body).title);
});
