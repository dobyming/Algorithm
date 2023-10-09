import sys
input = sys.stdin.readline

n,k = map(int,input().split())
result = list(map(int,input().split()))
shuffle = list(map(int,input().split()))

for _ in range(k):
    tmp = [0] * n 
    for i in range(n):
        tmp[shuffle[i]-1] = result[i]
    result = tmp

print(*result)