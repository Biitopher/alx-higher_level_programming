#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 4) {
  console.log('Usage: node starwars_title.js <movie_id> <episode_number>');
  process.exit(1);
}

const movieId = process.argv[2];
const episodeNumberToMatch = parseInt(process.argv[3], 10);
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    try {
      const movieData = JSON.parse(body);
      if (movieData.episode_id === episodeNumberToMatch) {
        console.log(movieData.title);
      } else {
        console.log(`No Star Wars movie found with Episode Number ${episodeNumberToMatch}`);
      }
    } catch (parseError) {
      console.error(parseError);
    }
  }
});

