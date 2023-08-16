#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
const newArray = list.map((mul, index) => mul * index);
console.log(newArray);
