#!/usr/bin/node
const request = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
function swapi (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
}
request(url, swapi);
