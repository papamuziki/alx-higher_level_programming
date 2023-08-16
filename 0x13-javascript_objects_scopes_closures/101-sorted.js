#!/usr/bin/node

const dict = require('./101-data').dict;
const dict1 = {};
for (const [key, value] of Object.entries(dict)) {
  if (!(value in dict1)) {
    dict1[value] = [key];
  } else {
    dict1[value].push(key);
  }
}
console.log(dict1);
