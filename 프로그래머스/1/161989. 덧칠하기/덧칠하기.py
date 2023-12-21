def solution(n, m, section):
    answer = 1
    # section에서 첫번째 구간은 무조건 포함 시킨다. 
    init = section[0]
    
    for s in section:
        if init + (m-1) < s:
            init = s
            answer += 1
        
    return answer