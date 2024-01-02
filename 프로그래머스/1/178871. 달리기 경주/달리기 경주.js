function solution(players, callings) {
    var answer = [];
    let p_dict = {}
    for(var i=0; i<players.length; i++){
        p_dict[players[i]] = i
    }
    
    for(var i=0; i<callings.length; i++){
        let idx = p_dict[callings[i]]
        p_dict[callings[i]] -= 1
        p_dict[players[idx-1]] += 1
        
        const temp = players[idx-1]
        players[idx-1] = players[idx]
        players[idx] = temp 
    }
    
    answer = players
    return answer;
}