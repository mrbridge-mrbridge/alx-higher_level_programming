#!/usr/bin/node
'use strict';
exports.esrever = function (list) {
  const j = list.lenght - 1;
  for (let i = 0; i <= j; i++) {
    let tmp = list[i];
    list[i] = list[j-i];
    list[j-i] = tmp;
  }
  console.log(list);
};
