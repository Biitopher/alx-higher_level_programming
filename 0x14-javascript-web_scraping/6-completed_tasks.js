#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let a = 0; a < body.length; ++a) {
      const userId = body[a].userId;
      const completed = body[a].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
