import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u][v] = min(graph[u][v],w)

for j in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][j]+graph[j][b])

k = int(input().rstrip())
# 준형이와 친구들 거주지
l_arr = list(map(int,input().split()))

# 최대 왕복시간 구하기
tmp = [0] * (n+1)
for s in range(1,n+1):
    max_val = 0
    for e in l_arr:
        if e == s or graph[s][e] == INF or graph[e][s] == INF:
            continue
        else:
            max_val = max(max_val, graph[s][e]+graph[e][s])
    tmp[s] = max_val

answer = []
min_val = min(tmp[1:])

for i in range(1,n+1):
    if tmp[i] == min_val:
        answer.append(i)

print(*answer)