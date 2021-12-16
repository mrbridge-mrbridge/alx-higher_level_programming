#!/usr/bin/node
'use strict';
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let args = process.argv.slice(2);
  args = args.sort().reverse();
  console.log(args[1]);
}
