#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
function swapi (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characts = (JSON.parse(body).characters);
    const size = characts.length;
    for (let step = 0; step < size; step++) {
      request(characts[step], function (error, response, body) {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
}
request(url, swapi);
