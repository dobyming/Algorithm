import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().rstrip())
dish = [list(map(int,input().split())) for _ in range(n)]
dish_comb = [combinations(dish,i) for i in range(1,n+1)]

answer = int(1e9)
for comb in dish_comb:
    for c in comb:
        sour = 1
        bitter = 0
        for s,e in c:
            sour *= s
            bitter += e
        answer = min(answer,abs(sour-bitter))

print(answer)