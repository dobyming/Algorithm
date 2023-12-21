function solution(n, m, section) {
    let answer = 1;
    let init = section[0]
    
    for(var i=0; i<section.length; i++) {
        if(init+(m-1) < section[i]){
            init = section[i]
            answer += 1
        }
    }
    return answer;
}