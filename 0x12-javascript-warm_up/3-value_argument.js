#!/usr/bin/node
'use strict';
const ag = process.argv[2];
if (ag === undefined) {
  console.log('No argument');
} else {
  console.log(ag);
}
