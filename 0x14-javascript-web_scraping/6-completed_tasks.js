#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completedTask = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completedTask[task.userId] === undefined) {
          completedTask[task.userId] = 1;
        } else {
          completedTask[task.userId]++;
        }
      }
    }
    console.log(completedTask);
  } else {
    console.log('Error occured. Status code: ' + response.statusCode);
  }
});
