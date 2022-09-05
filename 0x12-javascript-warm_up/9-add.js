#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  const sum = a + b;
  return sum;
}
console.log(add(num1, num2));
