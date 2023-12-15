function solution(cards1, cards2, goal) {
    var answer = '';
    
    let size = goal.length;
    let cnt = 0;
    
    for(var i=0; i<goal.length; i++){
        if(cards1.includes(goal[i])){
            c1 = cards1.shift()
            if(c1 === goal[i]) {
                cnt += 1
            } else {
                break
            }
        }
        else if(cards2.includes(goal[i])){
            c2 = cards2.shift()
            if(c2 === goal[i]) {
                cnt += 1
            } else {
                break
            }
        }
    }
    
    cnt === size ? answer = 'Yes' : answer = 'No'
    
    return answer;
}