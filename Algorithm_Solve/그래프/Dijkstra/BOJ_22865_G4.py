import sys,heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
# 친구들 사는 위치
A,B,C = map(int,input().split())
m = int(input().rstrip())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

def dijkstra(start):
    heap = []
    distance = [INF] * (n+1)
    heapq.heappush(heap,[0,start])
    distance[start] = 0

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

a_dist = dijkstra(A)
b_dist = dijkstra(B)
c_dist = dijkstra(C)

max_val, answer = 0,0
for j in range(1,n+1):
    if max_val < min(a_dist[j],b_dist[j],c_dist[j]):
        max_val = min(a_dist[j],b_dist[j],c_dist[j])
        answer = j 

print(answer)