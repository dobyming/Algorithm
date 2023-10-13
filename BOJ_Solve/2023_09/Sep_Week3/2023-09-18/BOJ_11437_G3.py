import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x,depth):
    visited[x] = True
    d[x] = depth
    for i in graph[x]:
        if visited[i]:
            continue
        parent[i] = x
        dfs(i,depth+1)


def lca(a,b):
    # depth 동일하게
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 부모가 같을때 까지 거슬러 올라감
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1) # 각 노드의 부모 노드 담김
d = [0] * (n+1) # 각 노드까지의 깊이
visited = [False] * (n+1) # 각 노드가 방문되었는지

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1,0) # 루트, depth

m = int(input().rstrip())
for _ in range(m):
    u,v = map(int,input().split())
    print(lca(u,v))