import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
# 각 분기점이 적의 시야에 보이는지 여부(0:안보임,1:보임)
sight = list(map(int,input().split()))
sight[-1] = 0 # n-1은 어쩔 수 없지만 도달하도록

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap,[0,start])

    while heap:
        d,now = heapq.heappop(heap)
        if distance[now] < d:
            continue
        for v,w in graph[now]:
            cost = d + w
            if sight[v] == 0 and cost < distance[v]:
                distance[v] = cost
                heapq.heappush(heap,[cost,v])
            
for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append([b,t])
    graph[b].append([a,t])

dijkstra(0)

if distance[n-1] != INF:
    print(distance[n-1])
else:
    print(-1)