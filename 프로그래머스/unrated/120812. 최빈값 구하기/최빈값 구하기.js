function solution(array) {
    let answer = 0;
    let map = new Map();
    
    // map을 활용하여 값이 몇개 있는지 define
    for(num of array){
        map.set(num,(map.get(num)||0)+1)
    }
    
    let cnt = 0
    let max_val = Math.max(...map.values())
    
    map.forEach((v,k) => {
        if(map.get(k) === max_val){
            cnt += 1
            answer = k
        }
    });
        
    cnt > 1 ? answer = -1 : answer 
    
    return answer;
}