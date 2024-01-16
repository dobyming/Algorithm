let [A,B] = require('fs').readFileSync('dev/stdin').toString().trim().split(" ");

let n = B.length - A.length + 1;
let answer = [];

for(var i=0; i<n; i++){
    let cnt = 0
    for(var j=0; j<A.length; j++){
        if(A[j] !== B[i+j]){
            cnt += 1;
        }
    }
    answer.push(cnt)
}

console.log(Math.min(...answer));