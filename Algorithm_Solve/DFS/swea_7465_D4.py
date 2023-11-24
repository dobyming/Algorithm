# 몇개의 무리가 존재하는지 return

T = int(input())
for i in range(1,T+1):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    visited = [False] * (n+1)

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(v):
        visited[v] = True
        for k in graph[v]:
            if not visited[k]:
                dfs(k)

    cnt = 0
    for j in range(1,n+1):
        if not visited[j]:
            dfs(j)
            cnt += 1

    print(f'#{i} {cnt}')