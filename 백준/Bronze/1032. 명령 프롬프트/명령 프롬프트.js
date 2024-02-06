const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input.shift());
let word = input.map((v)=>v.trim())
let first = word.shift().split('');

for (let i=0; i<word.length; i++) {
  for (let j=0; j<word[i].length; j++) {
    if (word[i][j] === first[j]) {
      continue;
    } else {
      first[j] = '?'
    }
  }
}

console.log(first.join(''));