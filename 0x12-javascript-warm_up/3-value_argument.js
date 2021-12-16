#!/usr/bin/node
'use strict';
let ag = process.argv[2];
if (ag === undefined) {
	console.log('No argument');
} else {
	console.log(ag);
}
