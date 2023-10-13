import sys 
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue.append(start)
    visited[start] = 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)
                

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
queue = deque([])

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []

for i in range(1,n+1):
    visited = [0] * (n+1)
    bfs(i)
    result.append(sum(visited)-n)

print(result.index(min(result))+1)