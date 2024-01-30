import sys
input = sys.stdin.readline

# 한번에 넣을 수 있는 최대 상자 개수 

answer = 0
n = int(input().rstrip())
arr = list(map(int,input().split()))
dp = [1] * (n+1)

for i in range(1,len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
            
print(max(dp))