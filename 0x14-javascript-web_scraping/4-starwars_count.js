#!/usr/bin/node
const request = require('request');
const starWarsApi = process.argv[2];
let times = 0;

request(starWarsApi, function (_error, response, body) {
  body = JSON.parse(body).data;

  for (let a = 0; a < body.length; ++a) {
    const characters = body[a].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
