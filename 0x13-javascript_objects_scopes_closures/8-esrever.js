#!/usr/bin/node
'use strict';
exports.esrever = function (list) {
  const arr = [];
  const j = list.length - 1;
  for (let i = j; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
