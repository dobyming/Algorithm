import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur):
    queue = deque([])
    queue.append(cur)
    visited = [0] * (n+1)
    visited[cur] = 1
    cnt =1 

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                cnt += 1
                visited[i] = 1
    
    return cnt

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]


# 해킹 관계는 반대로 생각해야함 
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

max_val = 1
result = []

for i in range(1,n+1):
    val = bfs(i)
    if val > max_val:
        max_val = val
        result.clear()
        result.append(i)
    elif val == max_val:
        result.append(i)

print(*result)
