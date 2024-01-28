const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

/**정답 제출 시에는 이 코드로 제출 */
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [n,m] = input.shift().split(' ').map(Number);
let board = input.slice(0).map((v) => v.trim().split(""));
let dx = [-1,1,0,0];
let dy = [0,0,-1,1];

const bfs = (i,j) => {
  let cnt = 0;
  let queue = [[i,j]];
  let color = board[i][j];
  board[i][j] = 0;

  while (queue.length) {
    let [x,y] = queue.shift();
    cnt += 1;

    for (let k=0; k<4; k++) {
      let nx = x+dx[k]
      let ny = y+dy[k]
      if (0<=nx && nx <m && 0<=ny && ny<n && color === board[nx][ny]) {
        board[nx][ny] = 0;
        queue.push([nx,ny]);
      }
    }
  }

  color === 'W' ? (w+=cnt**2) : (b+=cnt**2);
}

let w =0;
let b = 0;

for (let i=0; i<m; i++){
  for (let j=0; j<n; j++){
    if (board[i][j]) bfs(i,j)
  }
}

console.log(w + ' ' + b);