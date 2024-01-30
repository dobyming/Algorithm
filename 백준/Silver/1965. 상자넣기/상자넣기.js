const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

/**정답 제출 시에는 이 코드로 제출 */
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let n = Number(input.shift());
let arr = input[0].split(' ').map(Number);
let dp = new Array(n+1).fill(1);

for (let i=1; i<n; i++) {
  for (let j=0; j<i; j++) {
    if (arr[j] < arr[i]) {
      dp[i] = Math.max(dp[i],dp[j]+1);
    }
  }
}

console.log(Math.max(...dp))