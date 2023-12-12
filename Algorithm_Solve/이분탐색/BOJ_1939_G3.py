# n개의 섬으로 이루어진 나라가 있다. 
# 몇개의 섬 사이에는 다리가 설치되어 차들이 다닐 수 있음 
# 두개의 섬에 공장을 세워둠
# 각각의 다리마다 중량 제한이 있음 
# 한번의 이동에서 옮길 수 있는 물품둘의 중량의 최댓값 return 

import sys
input = sys.stdin.readline
from collections import deque

def bfs(target):
    queue = deque([])
    visited = [False] * (n+1)
    queue.append(f1)
    visited[f1] = True

    while queue:
        x = queue.popleft()
        for dst,w in graph[x]:
            if not visited[dst] and w >= target:
                queue.append(dst)
                visited[dst] = True
    
    if visited[f2]:
        return True
    
    return False

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)] 

for _ in range(m): 
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

f1,f2 = map(int,input().split())

s,e = 0,1000000000
answer = 0
while s<=e:
    mid = (s+e) // 2
    if bfs(mid):
        answer = mid 
        s = mid + 1
    else:
        e = mid - 1

print(answer)