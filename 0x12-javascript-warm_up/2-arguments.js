#!/usr/bin/node

const process = require('process');
const arg_num = process.argv.length;

if (arg_num < 0){
	console.log('No argument');
} else if (arg_num == 1) {
	console.log('Argument found');
} else if (arg_num > 1) {
	console.log('Arguments found');
}
