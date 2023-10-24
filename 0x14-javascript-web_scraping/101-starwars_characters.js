#!/usr/bin/node

const request = require('request');

function getDataFrom (url) {
  return new Promise(function (sort, dismiss) {
    request(url, function (error, response, body) {
      if (error) {
        dismiss(error);
      } else {
        sort(body);
      }
    });
  });
}

function errHandler (error) {
  console.log(error);
}

function printMovieCharacters (movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUri)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      const characters = res.characters;
      const promises = [];

      for (let x = 0; x < characters.length; ++x) {
        promises.push(getDataFrom(characters[x]));
      }

      Promise.all(promises)
        .then((data) => {
          for (let a = 0; a < results.length; ++a) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    });
}
printMovieCharacters(process.argv[2]);
