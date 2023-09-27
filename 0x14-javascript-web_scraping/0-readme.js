#!/usr/bin/node

// reads and prints the content of  file

// import filesystem(fs) module in node.js
const fs = require('fs');
// take arg provided and keep it in filename(fn) variable
const fn = process.argv[2];

fs.readFile(fn, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
