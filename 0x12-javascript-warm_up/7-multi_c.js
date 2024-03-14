#!/usr/bin/node

const numVar = parseInt(process.argv[2]);
if (isNaN(numVar)) {
  console.log('Missing number of occurences');
} else {
  let i;
  for (i = 0; i < numVar; i++) {
    console.log('C is fun');
  }
}
