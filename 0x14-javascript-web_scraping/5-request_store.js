#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
function store (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], response.body, 'utf8', error => {
      if (error) {
        console.log(error);
      }
    });
  }
}
request(url, store);
