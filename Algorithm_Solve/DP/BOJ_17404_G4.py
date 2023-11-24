import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
# 각 집별 R,G,B 비용 순서 
colors = [list(map(int,input().split())) for _ in range(n)]
result = INF

for i in range(3):
    dp = [[INF]*3 for _ in range(n)]
    dp[0][i] = colors[0][i]
    
    for j in range(1,n):
        dp[j][0] = colors[j][0] + min(dp[j-1][1],dp[j-1][2])
        dp[j][1] = colors[j][1] + min(dp[j-1][0],dp[j-1][2])
        dp[j][2] = colors[j][2] + min(dp[j-1][0],dp[j-1][1])
    
    for k in range(3):
        if i != k:
            result = min(result,dp[-1][k])

print(result)