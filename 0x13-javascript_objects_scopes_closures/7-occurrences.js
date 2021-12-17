#!/usr/bin/node
'use strict';
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const i of list) {
    if (i === searchElement) {
      count++;
    }
  }
  return count;
};
