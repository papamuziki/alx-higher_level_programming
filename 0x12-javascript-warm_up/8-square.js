#!/usr/bin/node

const size = process.argv[2];

if (!(Math.floor(size))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++){
      console.log('X');
    }
  }
}
