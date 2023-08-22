import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue.append(start)
    visited[start] = 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[x] + 1 

n = int(input().rstrip()) # 동기의 수
m = int(input().rstrip()) 
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
queue = deque([])

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

cnt = 0
for i in range(2,n+1):
    if visited[i] < 4 and visited[i] != 0:
        cnt += 1

print(cnt)