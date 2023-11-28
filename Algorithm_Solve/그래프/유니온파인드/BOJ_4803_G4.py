# 그래프가 주어졌을때 트리의 개수를 return 
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    isCycle = False
    q = deque()
    q.append(start)
    
    while q:
        x = q.popleft()
        if visited[x]:
            isCycle = True
        
        visited[x] = 1
        
        for adj_node in graph[x]:
            if visited[adj_node] == 0:
                q.append(adj_node)
                
    return isCycle

idx = 0
while True:
    # 정점,간선의 개수
    n,m = map(int,input().split())
    idx += 1
    if n == 0 and m == 0:
        break
    
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    cnt = 0 

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(n+1):
        if visited[i] == 0:
            if not bfs(i):
                cnt += 1
    cnt -=1 
   
    if cnt == 0:
        print(f'Case {idx}: No trees.')
    elif cnt == 1:
        print(f'Case {idx}: There is one tree.')
    else:
        print(f'Case {idx}: A forest of {cnt} trees.')