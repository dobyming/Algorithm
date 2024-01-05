def solution(bandage, health, attacks):
    answer = 0
    # 공격 정보 
    attack_dict = {}
    for attack,damage in attacks:
        attack_dict[attack] = damage
    
    t = 0
    consecutive = 0 # 연속 성공
    max_time = attacks[-1][0]
    max_health = health # 유지해야하는 체력 양 
    
    while t <= max_time:
        # 공격 time이 왔을때 
        if t in attack_dict:
            health -= attack_dict[t]
            consecutive = 0
            
            if health <= 0:
                return -1
        
        else:
            consecutive += 1
            # 연속시간이 시전시간에 도달하지 않았을때: 
            if consecutive < bandage[0]:
                health += bandage[1]
                if health > max_health:
                    health = max_health
            # 연속시간이 시전시간을 넘었을때 
            else:
                health += bandage[1] + bandage[2]
                if health > max_health:
                    health = max_health
                consecutive = 0 
        t += 1
        
    return health