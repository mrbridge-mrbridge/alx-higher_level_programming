#!/usr/bin/node
'use strict';
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
    	if (c) {
          console.log('C'.repeat(this.size));
	} else {
          console.log('X'.repeat(this.size));
	}
    }
  }
};
