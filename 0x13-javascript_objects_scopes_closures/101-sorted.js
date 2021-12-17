#!/usr/bin/node
'use strict';
const dict = require('./101-data.js').dict;
const newDict = {}; 
for (let key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
