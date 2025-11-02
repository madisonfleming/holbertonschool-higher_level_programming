#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
const sum = add(a, b);
console.log(sum);
