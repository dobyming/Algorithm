import sys
input = sys.stdin.readline
from itertools import combinations

N,L,R,X = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

cnt = 0
arr_comb = list(combinations(arr,i) for i in range(2,N+1))
for comb in arr_comb:
    for c in comb:
        if X <= c[-1] - c[0] and L <= sum(c) <= R:
            cnt += 1 

print(cnt)