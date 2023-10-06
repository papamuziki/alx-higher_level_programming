#!/usr/bin/node

const request = require('request');
const apiurl = process.argv[2];

request(apiurl, function(err, response, body){
  if (err){
    console.log(err);
  } else if (response.statusCode === 200){
    const completedTasks = {};
    const tasks = JSON.parse(body);
  
    for (let i in tasks){
      const task = tasks[i];
      if (task.completedTasks === true){
        if (completedTasks[task.userId] == undefined){
	  completedTasks[task.userId] = 1;
	} else {
	  completedTasks[task.userId]++;
	}
      }
    }
    console.log(completedTasks);
  }
});
