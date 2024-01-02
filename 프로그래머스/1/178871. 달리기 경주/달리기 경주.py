def solution(players, callings):
    answer = []
    p_dict = dict()
    
    for i in range(len(players)):
        p_dict[players[i]] = i
    
    for calling in callings:
        # 호명된 사람의 현재 등수를 저장하여 앞의 사람의 등수에도 영향을 주도록 
        idx = p_dict[calling] 
        p_dict[calling] -= 1
        p_dict[players[idx-1]] += 1
        # 교환 
        players[idx-1],players[idx] = players[idx],players[idx-1]
    
    tmp = list(p_dict.items())
    tmp.sort(key=lambda x:x[1])
    for a,b in tmp:
        answer.append(a)
        
    return answer