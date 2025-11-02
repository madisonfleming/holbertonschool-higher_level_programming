#!/usr/bin/node
const x = parseInt(process.argv[2]);
let line = '';
if (!isNaN(x)) {
  for (let i = 1; i <= x; i++) {
    line += 'X';
  }
  for (let j = 1; j <= x; j++) {
    console.log(line);
  }
} else {
  console.log('Missing size');
}
