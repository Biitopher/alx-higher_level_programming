#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
	const data = JSON.parse(body);
	console.log(results.reduce((count, movie) => {
      		return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
