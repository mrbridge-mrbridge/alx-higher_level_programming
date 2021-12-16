#!/usr/bin/node
'use strict';
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
