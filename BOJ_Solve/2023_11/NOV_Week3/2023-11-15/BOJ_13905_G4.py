import sys,heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드 수, 간선 수
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

# 출발 위치, 도착위치
s,e = map(int,input().split())
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

distance = [0] * (n+1)
heap = []

def dijkstra(start):
    heapq.heappush(heap,[-INF,start])
    distance[start] = INF

    while heap:
        d,now = heapq.heappop(heap)
        d = -d # maxheap으로 접근
        if distance[now] > d:
            continue
        for v,w in graph[now]:
            cost = min(d,w)
            if cost > distance[v]:
                distance[v] = cost
                heapq.heappush(heap,[-cost,v])

    return distance

tmp = dijkstra(s)
print(tmp[e])