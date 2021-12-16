#!/usr/bin/node
'use strict';
const arg = process.argv[2];
let i = 0;
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (i; i < arg; i++) {
    console.log('C is fun');
  }
}
