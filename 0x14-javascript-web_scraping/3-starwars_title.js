#!/usr/bin/node

// prints the title of a StarWars movie
// where the episode number matches a given integer

const req = require('request');
const movieID = process.argv[2];
const swapi = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

req(swapi, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const bodyContent = JSON.parse(body);
    console.log(bodyContent.title);
  }
});
