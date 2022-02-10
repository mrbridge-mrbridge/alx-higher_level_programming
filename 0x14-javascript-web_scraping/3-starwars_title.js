#!/usr/bin/node
const request = require('request');
let url = 'http://swapi-api.hbtn.io/ap/films/' + process.argv[2];
function swapi (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
}
request(url, swapi);
