const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let alphabet = 'abcdefghijklmnopqrstuvwxyz';
const INF = parseInt(1e9);    

/** Input 부 */
const n = parseInt(input[0]);
const n_info = input.slice(1,n+1);
const m = parseInt(input[n+1])
const m_info = input.slice(n+2);

let graph = Array.from(Array(26),() => Array(26).fill(INF));
// n개 관계 입력
n_info.forEach((tmp) => {
    let [s,e] = tmp.trim().split(" is ");
    let a = alphabet.indexOf(s);
    let b = alphabet.indexOf(e);
    graph[a][b] = 1;
});

// floyd-warshall
for(let k=0; k<26; k++){
    for(let i=0; i<26; i++){
        for(let j=0; j<26; j++){
            graph[i][j] = Math.min(graph[i][j],graph[i][k]+graph[k][j]);
        }
    }
}

m_info.forEach((tmp) => {
    let [r,c] = tmp.trim().split(" is ");
    let mx = alphabet.indexOf(r);
    let my = alphabet.indexOf(c);
    graph[mx][my] === INF ? console.log('F') : console.log('T');
});
