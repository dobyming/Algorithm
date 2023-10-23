import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int,input().split()))
dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(len(arr)-max(dp))