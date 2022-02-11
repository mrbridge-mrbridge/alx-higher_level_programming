#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characts = JSON.parse(body).characters;
    LoopThrough(characts, 0);
  }
});
function LoopThrough (characts, item) {
  request(characts[item], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      if (item + 1 < characts.length) {
        LoopThrough(characts, item + 1);
      }
    }
  });
}
