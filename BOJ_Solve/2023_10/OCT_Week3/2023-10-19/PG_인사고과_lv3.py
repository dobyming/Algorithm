def solution(scores):
    answer = 1
    target = scores[0]
    target_score = sum(scores[0])
    
    # 근무태도 내림차순, 동료평가 오름차순
    scores.sort(key=lambda x:(-x[0],x[1]))
    
    tmp = 0
    for a,b in scores:
        if target[0] < a and target[1] < b:
            answer = -1
            break
        if tmp <= b:
            tmp = b
            if a+b > target[0] + target[1]:
                answer += 1
        
    return answer