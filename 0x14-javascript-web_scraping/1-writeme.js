#!/usr/bin/node
const fs = require('fs');
fs.write(process.argv[2], process.argv[3],'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
