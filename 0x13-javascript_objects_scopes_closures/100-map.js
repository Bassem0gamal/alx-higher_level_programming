#!/usr/bin/node
import { list } from ('./100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
