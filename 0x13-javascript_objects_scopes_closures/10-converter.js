#!/usr/bin/node
'use strict';
exports.converter = function (base) {
  return num => num.toString(base);
};
