#!/usr/bin/node

const request = require('request');
const apiurl = process.argv[2];

request.get(apiurl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      const characters = films[i].characters;
      for (const j in characters) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
