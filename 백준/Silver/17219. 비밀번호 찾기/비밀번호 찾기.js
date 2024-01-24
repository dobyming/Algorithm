const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [n,m] = input[0].split(' ').map(Number);
let a_dict = new Map();

for(let i=1; i<n+1; i++){
    let [adrs,pwd] = input[i].split(' ');
    pwd = pwd.trim()
    a_dict.set(adrs,pwd);
}

for(let j=n+1; j<n+m+1; j++){
    let target = input[j].trim();
    console.log(a_dict.get(target));
}