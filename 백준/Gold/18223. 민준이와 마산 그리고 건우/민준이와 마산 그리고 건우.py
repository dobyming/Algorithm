import sys,heapq
input = sys.stdin.readline

# 출발지 : 1번 dijkstra 시작 지점 
# 마산 : v번 정점
# 건우: p번 정점

# 건우를 도와주는 경로 길이 <= 최단경로 길이 

n,e,p = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

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

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

# 1번 시작점 
f_dist = dijkstra(1)
# p번 시작점
p_dist = dijkstra(p)

if f_dist[p] + p_dist[n] <= f_dist[n]:
    print('SAVE HIM')
else:
    print('GOOD BYE')