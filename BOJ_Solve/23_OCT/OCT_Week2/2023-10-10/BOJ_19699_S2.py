import math
from itertools import combinations

n,m = map(int,input().split())
weights = list(map(int,input().split()))
MAX = 1001

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

weight_comb = list(combinations(weights,m))
answer = []
for comb in weight_comb:
    total = sum(comb)
    if isPrime(total):
        answer.append(total)

answer = list(set(answer))
answer.sort()

if len(answer) != 0:
    print(*answer)
else:
    print(-1)