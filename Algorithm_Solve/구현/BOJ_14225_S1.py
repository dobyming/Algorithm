import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input().rstrip())
arr = list(map(int,input().split()))

comb_arr = list(combinations(arr,i) for i in range(1,n+1))

result = []
for comb in comb_arr:
    for c in comb:
        result.append(sum(c))

m = max(result)
dp = [0] * (m+2)

for res in result:
    dp[res] += 1

for i in range(1,len(dp)):
    if dp[i] == 0:
        print(i)
        break