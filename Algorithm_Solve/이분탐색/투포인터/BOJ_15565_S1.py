# 라이언: 1, 어피치: 2 
# 라이언 인형이 k개 이상 있는 가장 작은 연속된 인형들의 집합 크기 return 

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))

s,e = 0,0
l_cnt = 0
answer = sys.maxsize

if arr[s] == 1:
    l_cnt += 1

while s<len(arr) and e<len(arr):
    if l_cnt < k:
        e += 1
        if e<len(arr) and arr[e] == 1:
            l_cnt += 1
    else:
        if l_cnt == k:
            answer = min(answer,e-s+1)
        if s < len(arr) and arr[s] == 1:
            l_cnt -= 1
        s += 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)