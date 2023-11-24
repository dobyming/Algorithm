import sys,heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [INF] * (n+1)
    heap = []
    # 항상 dijkstra에서 heap 사용시, 거리를 우선으로 넣는다.
    heapq.heappush(heap,[0,start]) # 거리,정점
    distance[start] = 0

    while heap:
        d,now = heapq.heappop(heap)
        if distance[now] < d:
            continue
        # 정점,거리 순서 
        for v,w in graph[now]:
            cost = d+w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(heap,[cost,v])
    
    return distance

n,e = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int,input().split())

# 출발점이 1,v1,v2일때
origin = dijkstra(1)
fromV1 = dijkstra(v1)
fromV2 = dijkstra(v2)

# 1->v1->v2->n
v1_path = origin[v1] + fromV1[v2] +fromV2[n]
# 1->v2->v1->n
v2_path = origin[v2] + fromV2[v1] + fromV1[n]

result = min(v1_path,v2_path)

if result < INF:
    print(result)
else:
    print(-1)

