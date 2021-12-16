#!/usr/bin/node
'use strict';
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
function add(a, b) {
  return (a + b)
}
console.log(add(a, b));
