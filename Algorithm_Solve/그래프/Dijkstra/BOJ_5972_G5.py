import sys,heapq
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

heap = []
def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    heapq.heappush(heap,[0,start])

    while heap:
        d,now = heapq.heappop(heap)
        if distance[now] < d:
            continue
        for v,w in graph[now]:
            cost = d+w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(heap,[cost,v])
    
    return distance

dist = dijkstra(1)
print(dist[n])