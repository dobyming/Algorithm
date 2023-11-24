import sys
sys.setrecursionlimit(10**3)

n = int(input())
# 능력치
board = [list(map(int,input().split())) for _ in range(n)]

visited = [0] * n
answer = 100*20

def dfs(depth):
    if depth == n:
        score()
        return
    visited[depth] = 1
    dfs(depth+1)
    visited[depth] = 0
    dfs(depth+1)

def score():
    global answer
    start,link = 0,0

    for i in range(n-1):
        for j in range(i+1,n):
            if visited[i] and visited[j]:
                start += board[i][j] + board[j][i]
            elif not visited[i] and not visited[j]:
                link += board[i][j] + board[j][i]
    
    tmp = abs(start-link)
    answer = min(answer,tmp)

dfs(0)
print(answer)