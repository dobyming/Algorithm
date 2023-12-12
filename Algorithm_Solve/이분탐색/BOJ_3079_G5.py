# 입국심사대는 N개, 친구는 M명
# 한 심사대에서는 한번에 한 사람만 심사를 받을 수 있다. 
# 빈 심사대로 가거나 더 바른 심사대의 심사가 끝나고 가도 된다. 
# 모든 사람이 심사를 받는데 최소의 시간 return 

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
time = [int(input().rstrip()) for _ in range(n)]

left = min(time)
right = max(time)*m
answer = right 

while left<=right:
    tmp = 0
    mid = (left+right) // 2

    # mid 시간에 받을 수 있는 인원 수 
    for i in range(n):
        tmp += mid // time[i]
    
    if tmp >= m:
        right = mid - 1
        answer = min(answer,mid)
    else:
        left = mid + 1

print(answer)