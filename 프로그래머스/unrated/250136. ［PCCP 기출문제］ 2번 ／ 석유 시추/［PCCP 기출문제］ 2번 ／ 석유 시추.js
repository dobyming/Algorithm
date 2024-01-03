function solution(land) {
    let answer = 0;
    // 가로,세로 크기 
    let n = land.length;
    let m = land[0].length;
    
    const queue = []
    const dx = [-1,1,0,0]
    const dy = [0,0,-1,1]

    const visited = Array.from(Array(n), () => Array(m).fill(false))
    const result = Array(m).fill(0)

    function bfs(i,j){
        queue.push([i,j])
        visited[i][j] = true
        let cnt = 0
        let sY = j
        let eY = j
        
        while(queue.length){
            const [x,y] = queue.shift()
            cnt += 1
            sY = Math.min(sY,y)
            eY = Math.max(eY,y)
            
            for(var k=0; k<4; k++){
                let nx = x+dx[k]
                let ny = y+dy[k]
                if(0<=nx && nx<n && 0<=ny && ny<m && !visited[nx][ny]){
                    if(land[nx][ny] === 1){
                        queue.push([nx,ny])
                        visited[nx][ny] = true
                    }
                }
            }
        }
        
        for(var i=sY; i<eY+1; i++){
            result[i] += cnt
        }
    }
    
    for(var i=0; i<n; i++){
        for(var j=0; j<m; j++){
            if(land[i][j] === 1 && !visited[i][j]){
                bfs(i,j)
            }
        }
    }
    
    answer = Math.max(...result)
    
    return answer;
}