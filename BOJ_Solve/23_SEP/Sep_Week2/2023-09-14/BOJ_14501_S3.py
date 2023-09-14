import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [0] * (n+1)
for i in range(n):
    for j in range(i+arr[i][0],n+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(max(dp))