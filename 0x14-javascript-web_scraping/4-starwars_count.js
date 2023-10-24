#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (_error, response, body) {
  body = JSON.parse(body).results;

  for (let x = 0; x < body.length; ++x) {
    const characters = body[x].characters;

    for (let a = 0; a < characters.length; ++a) {
      const character = characters[a];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
