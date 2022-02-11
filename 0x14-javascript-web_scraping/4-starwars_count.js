#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
function wedgeAntilles (error, response, body) {
  if (!error && response.statusCode === 200) {
    let count = 0;

    for (const x of JSON.parse(body).results) {
      for (const y of x.characters) {
        if (y === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
}
request(url, wedgeAntilles);
