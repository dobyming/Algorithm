import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue.append(start)
    visited[start] = True

    while queue:
        x = queue.popleft()
        if x == G:
            return cnt[G]
        for i in (x+U,x-D):
            if 0<i<=F and not visited[i]:
                cnt[i] = cnt[x] + 1
                visited[i] = True
                queue.append(i)
    if cnt[G] == 0:
        return "use the stairs"

F,S,G,U,D = map(int,input().split())
queue = deque([])
visited = [False] * (F+1)
cnt = [0] * (F+1)

print(bfs(S)) # 시작점