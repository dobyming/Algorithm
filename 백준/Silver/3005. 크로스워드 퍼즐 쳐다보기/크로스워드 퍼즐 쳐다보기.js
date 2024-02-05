const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

/**정답 제출 시에는 이 코드로 제출 */
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n,m] = input.shift().split(' ').map(Number);
let board = input.map((it) => it.trim().split(''))
let result = []

// 행일때
for (let i=0; i<n; i++) {
  let word = '';
  for (let j=0; j<m; j++) {
    if (board[i][j] !== '#') {
      word += board[i][j];
    } else {
      if (word.length > 1) {
        result.push(word);
        word = '';
      } else {
        word = '';
      }
    }
  }
  if (word.length > 1) {
    result.push(word)
  }
}

// js에서 2차원 배열 전환하는 법 
zip = rows => rows[0].map((_,c) => rows.map(row=>row[c]))
let z_board = zip([...board]);

// 열일때
for (let i=0; i<m; i++) {
  let z_word = '';
  for (let j=0; j<n; j++) {
    if (z_board[i][j] !== '#') {
      z_word += z_board[i][j];
    } else {
      if (z_word.length > 1) {
        result.push(z_word);
        z_word = '';
      } else {
        z_word = '';
      }
    }
  }
  if (z_word.length > 1) {
    result.push(z_word);
  }
}

result.sort();
console.log(result[0]);