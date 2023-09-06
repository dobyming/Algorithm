import sys
input = sys.stdin.readline

def dfs(start,depth):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            depth = dfs(i,depth+1)
    
    return depth

T = int(input().rstrip())

# 모든 국가를 방문하기 위한 최소 비행기 종류의 개수 return
for _ in range(T):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited[1] = True
    cnt = dfs(1,0)

    print(cnt)