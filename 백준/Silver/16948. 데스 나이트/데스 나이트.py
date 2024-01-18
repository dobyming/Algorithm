import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
r1,c1,r2,c2 = map(int,input().split())
flag = ''
board = [[0]*n for _ in range(n)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
queue = deque([])

def bfs(i,j):
    queue.append([i,j])

    while queue:
        x,y = queue.popleft()
        if x == r2 and y == c2:
            return True
        for k in range(6):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append([nx,ny])

    return False

flag = bfs(r1,c1)

if flag:
    print(board[r2][c2])
else:
    print(-1)