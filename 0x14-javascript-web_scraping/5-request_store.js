#!/usr/bin/node

const request = require('request');

request(process.argv[2]).pipe(require('fs').createWriteStream(process.argv[3]));
