const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

//bfs 함수
function bfs(i,j){
    queue.push([i,j]);
    visited[i][j] = true
    let v_cnt = 0;
    let k_cnt = 0;

    while(queue.length){
        let [x,y] = queue.shift();
        if(board[x][y] === 'v'){
            v_cnt += 1
        } else if(board[x][y] === 'k') {
            k_cnt += 1
        } 
        for(var k=0; k<4; k++){
            let nx = x+dx[k]
            let ny = y+dy[k]
            if(0<=nx && nx<R && 0<=ny && ny<C && !visited[nx][ny]){
                if(board[nx][ny] !== '#'){
                    queue.push([nx,ny]);
                    visited[nx][ny] = true
                }
            }
        }
    }

    k_cnt > v_cnt ? v_cnt = 0 : k_cnt = 0;

    return [v_cnt,k_cnt]
}

const [R,C] = input.shift().split(' ').map(Number);
const board = input.map((v) => v.split(''));

let visited = Array.from(Array(R),() => Array(C).fill(false));
let dx = [-1,1,0,0];
let dy = [0,0,-1,1];

let queue = [];

// 늑대와 양의 수
let v = 0;
let k = 0;

// 울타리가 아니면 bfs돌리기
for(var i=0; i<R; i++){
    for(var j=0; j<C; j++){
        if(board[i][j] !== '#' && !visited[i][j]) {
            let [v_cnt,k_cnt] = bfs(i,j)
            v += v_cnt
            k += k_cnt
        }
    }
}

console.log(k+' '+v);