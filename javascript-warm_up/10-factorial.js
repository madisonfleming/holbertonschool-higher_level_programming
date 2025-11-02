#!/usr/bin/node
function fact (n) {
  /* let counter = 1; */
  if (n < 0) {
    return -1;
  } else if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return (n * fact(n - 1));
  }
}
const myInt = Number(process.argv[2]);
console.log(fact(myInt));
