#!/usr/bin/node

// displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
