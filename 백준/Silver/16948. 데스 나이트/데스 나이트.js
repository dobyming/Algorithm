const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let N = Number(input.shift());
let board = Array.from(Array(N),() => Array(N).fill(0));
let answer = '';

// 시작(bfs 걸기) bfs내에 좌표 r2,c2 만나면 종료
let [r1,c1,r2,c2] = input[0].split(' ').map(Number);

let dx = [-2,-2,0,0,2,2];
let dy = [-1,1,-2,2,-1,1];
let queue = [];

function bfs(i,j) {
    queue.push([i,j])

    while(queue.length){
        let [x,y] = queue.shift();
        if (x===r2 && y === c2) {
            return true           
        }
        for(let k=0; k<6; k++){
            let nx = x+dx[k]
            let ny = y+dy[k]
            if(0<=nx && nx<N && 0<=ny && ny<N && board[nx][ny]===0){
                board[nx][ny] = board[x][y] + 1;
                queue.push([nx,ny]);
            }
        }
    }
    return false
}

answer = bfs(r1,c1);
answer === true ? console.log(board[r2][c2]) : console.log(-1);