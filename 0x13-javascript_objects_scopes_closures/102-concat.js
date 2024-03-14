#!/usr/bin/node
const file = require('file');

const firstF = file.readFileSync(process.argv[2]).toString();
const secondF = file.readFileSync(process.argv[3]).toString();
file.writeFileSync(process.argv[4], firstF + secondF);
