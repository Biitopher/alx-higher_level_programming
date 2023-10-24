#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./wedge_antilles_movies.js <API_URL>');
} else {
  const apiUrl = process.argv[2];

  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body);
      const wedgeAntillesMovies = data.results.filter((movie) =>
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );

      console.log(`Number of movies with Wedge Antilles: ${wedgeAntillesMovies.length}`);
    } else {
      console.error(`Error: ${error || 'API request failed'}`);
    }
  });
}
