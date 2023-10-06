#!/usr/bin/node

// prints the number of movies where the character
// Wedge Antilles is present

const re = require('request');
const url = process.argv[2];

re(url, function (err, body, response) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body).res;

    const moviesWithWedgeChar = res.reduce((count, movie) => {
      return movie.characters.find((characters) => character.endswith('/18/'))
        ? count + 1
        : count;
    }, 0);
    console.log(moviesWithWedgeChar);
  }
});
