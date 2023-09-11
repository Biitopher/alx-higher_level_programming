#!/usr/bin/node

const arg1 = process.argv[2];
const size = parseInt(arg1);

if (!isNaN(size)) {
  if (size <= 0) {
    console.log('Size must be a positive integer.');
  } else {
    for (let a = 0; a < size; a++) {
      let row = '';
      for (let b = 0; b < size; b++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
