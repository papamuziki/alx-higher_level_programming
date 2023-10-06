#!/usr/bin/node

// prints all characters of a Star Wars movie

const req = require('request');
const movieId = process.argv[2];
const swapi = 'https://swapi-api.alx-tools.com/api/people/';

function starWarsMovieChars(movieId, swapi){
  req.get(swapi, function (err, response, body){
    if (err) {
      console.log(err);
    }
    const jsonObject = JSON.parse(body);
    const people = jsonObject.results;
    for (let i in people) {
      for (j in people[i].films){
        if (people[i].films[j].includes(movieId)){
        console.log(people[i].name);
        }
      }
    }
    if (jsonObject.next !== null){
      starWarsMovieChars(movieId, jsonObject.next);
    }
  });
}
starWarsMovieChars(movieId, swapi);
