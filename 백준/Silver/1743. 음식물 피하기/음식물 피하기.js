const fs = require('fs');
/**정답 제출 시에는 이 코드로 제출 */
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let answer = [];

function bfs(i,j){
    queue.push([i,j]);
    visited[i][j] = true;
    let size = 1; // 음식물 크기 

    while(queue.length){
        let [x,y] = queue.shift();
        for(let k=0; k<4; k++){
            let nx = x+dx[k]
            let ny = y+dy[k]
            if(0<=nx && nx<n && 0<=ny && ny<m && !visited[nx][ny]){
                if(board[nx][ny] === '#'){
                    size += 1
                    queue.push([nx,ny])
                    visited[nx][ny] = true
                } else {
                    continue
                }
            }
        }
    }

    return size;
}

const [n,m,_] = input.shift().split(' ').map(Number);
let board = Array.from(Array(n),() => Array(m).fill('.'));
let visited = Array.from(Array(n),() => Array(m).fill(false));

input.forEach((v) => {
    let [vx,vy] = v.split(' ').map(Number);
    // 음식물 쓰레기(#) 배치하기
    board[vx-1][vy-1] = '#';
});

let dx = [-1,1,0,0];
let dy = [0,0,-1,1];
let queue = [];

for(let r=0; r<n; r++){
    for(let c=0; c<m; c++){
        if(board[r][c] === '#' && !visited[r][c]){
            let cnt = bfs(r,c);
            answer.push(cnt)
        }
    }
}

console.log(Math.max(...answer));