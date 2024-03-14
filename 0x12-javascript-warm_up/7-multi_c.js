#!/usr/bin/node

const numVar = parseInt(process.arg[2]);
if (isNaN(numVar)) {
  console.log('Missing number of instances');
} else {
  let i;
  for (i = 0; i < numVar; i++) {
    console.log('C is fun');
  }
}
