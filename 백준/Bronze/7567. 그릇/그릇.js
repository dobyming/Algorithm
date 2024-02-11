const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

/**정답 제출 시에는 이 코드로 제출 */
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const arr = input[0].split('');
let answer = 0;

for (let i=0; i<arr.length; i++) {
    if (i === 0) {
        answer += 10;
    }
    else if (arr[i] === arr[i-1]) {
        answer += 5;
    } else {
        answer += 10;
    }
}

console.log(answer);