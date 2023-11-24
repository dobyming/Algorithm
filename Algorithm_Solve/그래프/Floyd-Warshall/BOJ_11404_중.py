import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신은 0으로
for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u][v] = min(graph[u][v],w)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()