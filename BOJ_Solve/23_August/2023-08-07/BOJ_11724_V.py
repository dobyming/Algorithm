import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) # 정점별 방문여부 check

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)

# 기록
# 23.08.09 (OK)