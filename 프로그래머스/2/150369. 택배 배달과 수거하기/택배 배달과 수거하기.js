function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let r_deliveries = deliveries.reverse()
    let r_pickups = pickups.reverse()
    
    let tmp_d = 0
    let tmp_p = 0
    
    for(var i=0; i<n; i++){
        tmp_d += r_deliveries[i]
        tmp_p += r_pickups[i]
        while(tmp_d>0 || tmp_p >0){
            tmp_d -= cap
            tmp_p -= cap
            answer += (n-i) * 2
        }
    }
    return answer;
}