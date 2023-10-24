#!/usr/bin/node
const request = require('request');
const starWarsUrl = process.argv[2];

request(starWarsUrl, (error, response, body) {
	if (error) console.log(error);
	const times = character.split('/people/18').length - 1;
	console.log(times);
});
