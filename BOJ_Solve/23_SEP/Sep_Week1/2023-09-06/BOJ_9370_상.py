import sys,heapq
input = sys.stdin.readline

T = int(input().rstrip())
INF = int(1e9)

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

for _ in range(T):
    # 교차로,도로,목적지 후보의 개수
    n,m,t = map(int,input().split())
    # s는 예술가 출발지 , g-h(범인이 지나간 위치)
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append([b,d]) # 정점,길이
        graph[b].append([a,d])
    
    # 목적지 후보 
    dst = [int(input().rstrip()) for _ in range(t)]
    
    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    answer = []
    for k in dst:
        if s_[g]+g_[h]+h_[k] == s_[k] or s_[h]+h_[g]+g_[k] == s_[k]:
            answer.append(k)
    answer.sort()
    print(*answer)