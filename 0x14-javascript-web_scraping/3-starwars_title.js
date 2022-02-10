#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/ap/films/' + process.argv[2];
function swapi (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response) {
    console.log(response);
  }
  if (body) {
    console.log(JSON.parse(body).title);
  }
}
request(url, swapi);
