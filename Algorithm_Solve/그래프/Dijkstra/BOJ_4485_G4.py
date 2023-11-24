import sys,heapq
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra():
    heap = []
    # 가중치,x,y
    heapq.heappush(heap,[board[0][0],0,0])
    distance[0][0] = 0

    while heap:
        d,x,y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            print(f'Problem {t}: {distance[x][y]}')
            break
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                tmp = d + board[nx][ny]
                if tmp < distance[nx][ny]:
                    distance[nx][ny] = tmp
                    heapq.heappush(heap,[tmp,nx,ny])

t = 1
while True:
    n = int(input().rstrip())
    if n == 0:
        break
    board = [list(map(int,input().split())) for _ in range(n)]
    distance = [[INF]*n for _ in range(n)]

    cnt = dijkstra()
    t+=1