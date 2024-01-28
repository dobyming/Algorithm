const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [n,c] = input.shift().split(' ').map(Number);
let arr = input[0].split(' ').map(Number)

let result = [];
const freqMap = new Map();

for (let i=0; i<n; i++) {
  freqMap.set(arr[i],(freqMap.get(arr[i])||0)+1);
}

const sortedMap = [...freqMap].sort((a,b) => b[1]-a[1]);
sortedMap.map((info) => {
  let [k,v] = [info[0], info[1]];
  let tmp = 0;
  while (tmp < v) {
    result.push(k);
    tmp += 1;
  }
})

for (let j=0; j<result.length; j++) {
  process.stdout.write(result[j] + ' ')
}