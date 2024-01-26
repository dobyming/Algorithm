const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let n = Number(input.shift());
let arr = input[0].split(' ').map(Number);

let cnt = 0;
let result = 0;

for(let i=0; i<n; i++){
    if(arr[i] === 1){
        cnt += 1;
        result += cnt;
    } else {
        cnt = 0;
    }
}

console.log(result);