#!/usr/bin/node
const fs = require('fs');

const firstF = file.readFileSync(process.argv[2]).toString();
const secondF = file.readFileSync(process.argv[3]).toString();
file.writeFileSync(process.argv[4], firstF + secondF);
