#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  const first = args[0];
  let res = null;

  for (let i = 1; i < args.length; i++) {
    if (args[i] < first) {
      res = args[i];
      break;
    }
  }

  console.log(res !== null ? res : 0);
}
