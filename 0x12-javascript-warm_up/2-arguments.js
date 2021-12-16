#!/usr/bin/node
'use strict';
import { argv } from 'process';
let num = process.argv.length;
if (num === 2){
	console.log("No argument");
}
if (num === 3){
        console.log("Argument found");
}
if (num > 3){
        console.log("Arguments found");
}
