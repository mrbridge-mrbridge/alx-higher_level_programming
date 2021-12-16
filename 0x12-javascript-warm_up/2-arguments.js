#!/usr/bin/node
'use strict';
let num = process.argv.length;
if (num === 2) {
	console.log('No argument');
} else if (num === 3) {
        console.log('Argument found');
} else {
        console.log('Arguments found');
}
