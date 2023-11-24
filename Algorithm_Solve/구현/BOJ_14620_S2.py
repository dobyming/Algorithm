import sys
input = sys.stdin.readline
from itertools import combinations
    
n = int(input().rstrip())
answer = int(1e9)
price = [list(map(int,input().split())) for _ in range(n)]
candidates = [(r,c) for r in range(1,n-1) for c in range(1,n-1)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(arr):
    global answer
    visited = [[False]*n for _ in range(n)]
    amount = 0
    for x,y in arr:
        visited[x][y] = True
        amount += price[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                amount += price[nx][ny]
            else:
                return
    answer = min(answer,amount)

for c in combinations(candidates,3):
    check(c)

print(answer)