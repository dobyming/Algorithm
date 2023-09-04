import sys,heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [INF] * (n+1)
    heap = []
    heapq.heappush(heap,[0,start])
    distance[start] = 0

    while heap:
        d,now = heapq.heappop(heap)
        if distance[now] < d:
            continue
        for v,w in graph[now]:
            cost = d + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(heap,[cost,v])
    
    return distance

# x번 마을에 모여 파티를 벌임
n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

answer = 0
for i in range(1,n+1):
    tmp_s = dijkstra(i)
    tmp_e = dijkstra(x)
    answer = max(answer,tmp_s[x] + tmp_e[i])

print(answer)