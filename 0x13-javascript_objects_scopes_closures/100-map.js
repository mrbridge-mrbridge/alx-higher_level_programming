#!/usr/bin/node
'use strict';
let i;
const list = require('./100-data.js').list;
const newList = list.map((x, index) => x * index);
console.log(list);
console.log(newList);
