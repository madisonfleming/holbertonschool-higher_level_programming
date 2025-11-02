#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  console.log('My number:', parseInt(process.argv[2]));
} else if (process.argv.length <= 3) {
  console.log('Not a number');
}
