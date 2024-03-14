#!/usr/bin/node

// Prints two arguments passed to it, in the following format: “ is ”

const twoArgs = process.argv;
console.log(twoArgs[2], 'is', twoArgs[3]);
