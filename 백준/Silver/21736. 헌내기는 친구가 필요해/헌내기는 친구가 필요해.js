const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

// 도연이가 만날 수 있는 사람의 수 출력 
// O: 빈공간, x:벽, I: 도연이 , P: 사람
function bfs(i,j){
    queue.push([i,j]);
    visited[i][j] = true
    let cnt = 0;  

    while(queue.length){
        let [x,y] = queue.shift();
        for(let k=0; k<4; k++){
            let nx = x+dx[k]
            let ny = y+dy[k]
            if(0<=nx && nx<n && 0<=ny && ny<m && !visited[nx][ny]){
                if(board[nx][ny] === 'O'){
                    queue.push([nx,ny]);
                    visited[nx][ny] = true
                }
                else if(board[nx][ny] === 'P'){
                    cnt += 1
                    queue.push([nx,ny]);
                    visited[nx][ny] = true
                } 
                else if(board[nx][ny] === 'X'){
                    continue;
                }
            }
        }
    }

    return cnt; 
}

const [n,m] = input.shift().split(' ').map(Number);
const board = input.map(v => v.split(''))

let visited = Array.from(Array(n),() => Array(m).fill(false));
let queue = [];

let dx = [-1,1,0,0];
let dy = [0,0,-1,1];
let answer = 0;

for(let i=0; i<n; i++){
    for(let j=0; j<m; j++){
        if(board[i][j] === 'I'){
            cnt = bfs(i,j);
            answer += cnt;
        }
    }
}

if(answer === 0){
    console.log('TT');
} else {
    console.log(answer);
}