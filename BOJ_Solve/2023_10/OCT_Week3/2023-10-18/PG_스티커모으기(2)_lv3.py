def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        answer = sticker[0]
    else:
        dp1,dp2 = [0]*len(sticker), [0]*len(sticker)
        dp1[0] = sticker[0]
        dp1[1] = dp1[0]

        for i in range(2,len(sticker)-1):
            dp1[i] = max(dp1[i-1],sticker[i]+dp1[i-2])

        for j in range(1,len(sticker)):
            dp2[j] = max(dp2[j-2]+sticker[j],dp2[j-1])

        answer = max(dp1[-2],dp2[-1])
    
    return answer