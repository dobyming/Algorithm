function solution(bandage, health, attacks) {
    let answer = 0
    let attack_dict = new Map()
    for(var i=0; i<attacks.length; i++){
        attack_dict.set(attacks[i][0],attacks[i][1])
    }
    
    let t = 0 
    let c_time = 0
    let max_time = attacks[attacks.length-1][0]
    let max_health = health
    
    while(t<=max_time){
        // t가 attack_dict에 있을때
        if(attack_dict.has(t)){
            health -= attack_dict.get(t)
            c_time = 0
            if(health<=0){
                return -1
            }
        } else {
            c_time += 1
            if(c_time < bandage[0]) {
                health += bandage[1]
                if(health > max_health){
                    health = max_health
                }
            } else {
                health += bandage[1] + bandage[2]
                if(health>max_health){
                    health = max_health
                }
                c_time = 0
            }
        }
        t += 1
    }
    return health;
}