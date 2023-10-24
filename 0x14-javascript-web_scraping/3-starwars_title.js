#!/usr/bin/node
const request = require('request');
let url = 'https://swapi-api.alx-tools.com/api/films/1/' + process.argv[2];
request(url, function (err, response, body) {
  console.log(err || JSON.parse(body).title);
});
