#!/usr/bin/node
const { argv } = require('process');
const occurences = Number(argv[2]);
const display = () => {
  for (let i = 0; i < occurences; i++) {
    console.log('C is fun');
  }
};
isNaN(occurences)
  ? (console.log('Missing number of occurrences'))
  : (display());
