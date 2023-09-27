#!/usr/bin/node

// writes a string to a file

// import filesystem(fs) module in node.js
const fs = require('fs');
const filename = process.argv[2];
const newString = process.argv[3];

fs.writeFile(filename, newString, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
