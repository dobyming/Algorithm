function solution(name, yearning, photo) {
    var answer = [];
    let p_dict = {}
    
    for(var i=0; i<name.length; i++) {
        p_dict[name[i]] = yearning[i]
    }
    
    for(var i=0; i<photo.length; i++){
        let score = 0
        for(var j=0; j<photo[i].length; j++){
            if(Object.keys(p_dict).includes(photo[i][j])){
                score += p_dict[photo[i][j]]
            } else {
                continue
            }
        }
        answer.push(score)
    }
    
    return answer;
}