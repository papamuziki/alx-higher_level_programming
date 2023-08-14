#!/usr/bin/node

const process = require('process');
const argv = process.argv;

for (let i = 0; i < argv - 1; i++){
	if (argv === null){
		console.log('No argument');
	}
	console.log(argv[0]);
}
