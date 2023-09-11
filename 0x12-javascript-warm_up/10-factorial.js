#!/usr/bin/node

function factorial(n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg1 = process.argv[2];
const num = parseInt(arg1);
const result = factorial(num);
console.log(result);
