def solution(name, yearning, photo):
    answer = []
    # 인물의 그리움 점수를 모두 합산 = 해당 사진의 추억 점수 
    info = list(zip(name,yearning))
    i_dict = {}
    
    for name,score in info:
        i_dict[name] = score
    
    for p_arr in photo:
        score = 0
        for p in p_arr:
            if p in i_dict:
                score += i_dict[p]
            else:
                continue
        answer.append(score)
        
    return answer