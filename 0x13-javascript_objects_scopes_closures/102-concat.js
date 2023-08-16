#!/usr/bin/node

const fs = require('fs');
const x = fs.readFileSync(`./${process.argv[2]}`);
const y = fs.readFileSync(`./${process.argv[3]}`);
fs.appendFileSync(`./${process.argv[4]}`, x + y);
