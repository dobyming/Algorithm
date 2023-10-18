import heapq
INF = int(1e9)
def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for _ in range(n+1)]
    for u,v,w in fares:
        graph[u].append([v,w])
        graph[v].append([u,w])
    
    heap = []
    def dijkstra(start):
        distance = [INF] * (n+1)
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
    
    # i번 노드에서 임의 노드까지 갈 수 있는 최단경로를 모두 구한다. (중간지점 구하기)
    dist = [[]]
    for i in range(1,n+1):
        dist.append(dijkstra(i))
    
    # 출발지는 s, 각 도착지는 a와 b
    for i in range(1,n+1):
        answer = min(answer,dist[s][i]+dist[i][a]+dist[i][b])    
    
    return answer