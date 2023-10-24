#!/usr/bin/node
const request = require('request');
const starWarsApi = process.argv[2];

request(starWarsApi, function (error, response, body) {
	if (error) console.log(error);
	const times = character.split('/people/18').length - 1;
	console.log(times);
});
