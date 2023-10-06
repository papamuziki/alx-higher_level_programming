#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const apiurl = process.argv[2];
const fileName = process.argv[3];

request.get(apiurl, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(fileName, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
