#!/usr/bin/node
const request = require('request');
function res (response) {
  console.log('code: ', response.statusCode);
}
request.get(process.argv[2]).on('response', res);
