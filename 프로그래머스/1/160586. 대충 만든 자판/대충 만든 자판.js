function solution(keymap, targets) {
    var answer = [];
    let k_dict = {}
    
    for(var i=0; i<keymap.length; i++){
        for(var j=0; j<keymap[i].length; j++){
            if(Object.keys(k_dict).includes(keymap[i][j])){
                if(k_dict[keymap[i][j]] > j+1){
                    k_dict[keymap[i][j]] = j+1
                } else {
                    continue
                }
            } else {
                k_dict[keymap[i][j]] = j+1
            }
        }
    }
    
    for(var k=0; k<targets.length; k++){
        let result = 0
        for(var l=0; l<targets[k].length; l++){
            if(!Object.keys(k_dict).includes(targets[k][l])){
                result = -1
                break
            } else {
                result += k_dict[targets[k][l]]
            }
        }
        answer.push(result)
    }
    return answer;
}