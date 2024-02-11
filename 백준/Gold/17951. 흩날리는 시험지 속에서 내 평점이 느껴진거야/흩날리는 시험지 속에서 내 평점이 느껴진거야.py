import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))

answer = 0
left,right = 0,int(1e5)*20+1
while left <=right:
    mid = (left+right) // 2
    group = 0
    score = 0
    for a in arr:
        score += a
        if mid <= score:
            group += 1
            score = 0
    
    if group >= k:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)