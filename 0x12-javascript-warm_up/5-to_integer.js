#!/usr/bin/node

const arg1 = process.argv[2];
const parsedArg1 = parseInt(arg1);

if (!isNaN(parsedArg1)) {
  console.log(`My number: ${parsedArg1}`);
} else {
  console.log('Not a number');
}
