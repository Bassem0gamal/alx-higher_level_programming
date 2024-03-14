#!/usr/bin/node
const list = require('./100-data.js');
console.log(list);
const i = list.map((item, index) => item * index);
console.log(i);
