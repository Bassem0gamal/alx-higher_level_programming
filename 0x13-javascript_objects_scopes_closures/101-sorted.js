#!/usr/bin/node
const list = require('./101-data.js').dict;

const newlist = {};

for (const key in list) {
  if (newlist[list[key]] === undefined) newlist[list[key]] = [];
  newlist[list[key]].push(key);
}
console.log(newlist);
