#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
