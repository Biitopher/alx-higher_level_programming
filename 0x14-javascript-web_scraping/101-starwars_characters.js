#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./star_wars_characters.js <Movie ID>');
  process.exit(1);
}

const baseUrl = 'https://swapi.dev/api/films/';

request(`${baseUrl}${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);

    if (movieData.characters && Array.isArray(movieData.characters)) {
      console.log(`Characters in ${movieData.title} (${movieData.release_date}):`);

      function fetchCharacter(index) {
        if (index >= movieData.characters.length) {
          return;
        }

        request(movieData.characters[index], (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            fetchCharacter(index + 1);
          } else {
            console.error('Error fetching character data:', charError);
          }
        });
      }

      fetchCharacter(0);
    } else {
      console.error('No character data found in the movie.');
    }
  } else {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
  }
});
