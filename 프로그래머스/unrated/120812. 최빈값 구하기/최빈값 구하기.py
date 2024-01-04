from collections import Counter
def solution(array):
    answer = 0
    a_dict = Counter(array)
    max_val = max(a_dict.values())
    
    cnt = 0
    for k in a_dict:
        if a_dict[k] == max_val:
            cnt += 1
            answer = k
            
    if cnt > 1:
        answer = -1
        
    return answer