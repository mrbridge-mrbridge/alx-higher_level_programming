#!/usr/bin/node
'use strict';
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('x'.repeat(arg));
  }
}
