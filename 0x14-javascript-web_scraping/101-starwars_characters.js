#!/usr/bin/node

const request = require('request');

function getDataFrom (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(body);
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
          for (let a = 0; a < data.length; ++a) {
            console.log(JSON.parse(data[a]).name);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    });
}
printMovieCharacters(process.argv[2]);
