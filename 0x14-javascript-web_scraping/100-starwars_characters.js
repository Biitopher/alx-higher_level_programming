#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (error, response, body) {
  const characters = JSON.parse(body).characters;

  for (let a = 0; a < characters.length; ++a) {
    request(characters[a], function (_cError, _cResponse, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
