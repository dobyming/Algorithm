def solution(keymap, targets):
    answer = []
    k_dict = {}
    
    for key in keymap:
        for k in range(len(key)):
            if key[k] in k_dict:
                k_dict[key[k]] = min(k+1,k_dict[key[k]])
            else:
                k_dict[key[k]] = k+1
    
    for target in targets:
        result = 0
        for t in target:
            if t in k_dict:
                result += k_dict[t]
            else:
                result = -1
                break
        answer.append(result)
            
    return answer