import sys
input = sys.stdin.readline

def go(idx,total):
    if total < 0:
        return -9876543210
    if idx == n:
        return 0
    if dp[idx][total] != 0:
        return dp[idx][total]
    
    dp[idx][total] = max(go(idx+1,total-info[idx][0])+info[idx][1],go(idx+1,total-info[idx][2])+info[idx][3])
    
    return dp[idx][total]

n,k = map(int,input().split())
info = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n)]

print(go(0,k))