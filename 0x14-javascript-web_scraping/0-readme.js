#!/usr/bin/node

require('fs').readFile(process.argv[2], 'utf8', function (error, content) {
    console.log(error || content);
});
