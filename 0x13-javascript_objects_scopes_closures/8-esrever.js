#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const p = list[len];
    list[len] = list[i];
    list[i] = p;
    i++;
    len--;
  }
  return list;
};
