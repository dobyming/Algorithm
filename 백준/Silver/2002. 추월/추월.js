const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let s_rect = new Map();
let answer = 0;

const n = parseInt(input[0]);
const inArr = input.slice(1,n+1);
const outArr = input.slice(n+1);

for(let i=0; i<n; i++){
    s_rect.set(inArr[i].trim(),i);
}

for(let j=0; j<n-1; j++){
    for(let k=j; k<n; k++){
        if (s_rect.get(outArr[j].trim()) > s_rect.get(outArr[k].trim())){
            answer += 1
            break
        }
    }
}

console.log(answer);