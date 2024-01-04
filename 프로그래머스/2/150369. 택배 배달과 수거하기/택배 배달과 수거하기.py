def solution(cap, n, deliveries, pickups):
    answer = 0
    info = list(zip(deliveries,pickups))[::-1]
    
    tmp_d,tmp_p = 0,0
    for i in range(n):
        tmp_d += info[i][0]
        tmp_p += info[i][1]
        while tmp_d > 0 or tmp_p > 0:
            tmp_d -= cap
            tmp_p -= cap
            answer += (n-i) * 2
    
    return answer