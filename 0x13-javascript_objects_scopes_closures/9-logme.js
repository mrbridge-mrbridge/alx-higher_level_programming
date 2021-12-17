#!/usr/bin/node
'use strict';
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': '+ item);
  count++;
};
