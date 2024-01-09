function solution(begin, target, words) {
    let answer = 0;
    let visited = Array(words.length).fill(false)
    
    if(!words.includes(target)){
        return 0;
    }
    
    let queue = [];
    queue.push([begin,0]);

    while(queue){
        let [word,cnt] = queue.shift()
        
        if(word === target){
            answer = cnt
            break
        } else {
            for(var i=0; i<words.length; i++){
                let tmp_cnt = 0
                if(!visited[i]){
                    for(var j=0; j<words.length; j++){
                        if(word[j] !== words[i][j]) {
                            tmp_cnt += 1
                        }
                    }
                }
                if(tmp_cnt === 1){
                    queue.push([words[i],cnt+1])
                    visited[i] = true
                }
            }
        }
    }
    return answer;
}