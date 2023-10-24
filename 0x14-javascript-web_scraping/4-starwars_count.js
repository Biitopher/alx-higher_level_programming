#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body).data;
    console.log(data.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? times + 1
        : times;
    }, 0));
  }
});
