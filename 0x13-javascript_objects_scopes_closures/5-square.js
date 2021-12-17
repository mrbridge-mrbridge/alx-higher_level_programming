#!/usr/bin/node
'use strict';
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super (size, size);
    this.size = size;
  }
};
