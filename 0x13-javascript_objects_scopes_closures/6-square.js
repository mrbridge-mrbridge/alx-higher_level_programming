#!/usr/bin/node
'use strict';
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
