const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let INF = Number(1e9);

let [V,E,P] = input[0].split(' ').map(Number);
let graph = Array.from(Array(V+1),() => Array())

for(let i=1; i<E+1; i++){
    let [a,b,c] = input[i].split(' ').map(Number);
    graph[a].push([b,c]);
    graph[b].push([a,c]);
}

function dijkstra(start){
    let heap = []
    let distance = new Array(V+1).fill(INF);
    heap.push([0,start]);
    distance[start] = 0;

    while(heap.length){
        let [d,now] = heap.shift();
        if(distance[now] < d){
            continue
        }
        for(let [v,w] of graph[now]) {
            let cost = d+w;
            if(cost < distance[v]) {
                distance[v] = cost;
                heap.push([cost,v]);
            }
        }
    }
    return distance;
}

let f_dist = dijkstra(1);
let p_dist = dijkstra(P);

if (f_dist[P] + p_dist[V] <= f_dist[V]) {
    console.log('SAVE HIM');
} else {
    console.log('GOOD BYE');
}