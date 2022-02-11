#!/usr/bin/node
const request = require('request');
function tasksCompleted (error, response, body) {
  if (!error && response.statusCode === 200) {
    const members = JSON.parse(body);
    const compList = {};
    for (const item of members) {
      if (item.completed && compList[item.userId] === undefined) {
        compList[item.userId] = 1;
      } else if (item.completed) {
        compList[item.userId] += 1;
      }
    }
    console.log(compList);
  }
}
request(process.argv[2], tasksCompleted);
