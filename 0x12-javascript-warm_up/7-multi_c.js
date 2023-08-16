#!/usr/bin/node

if (!(Math.floor(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Math.floor(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
