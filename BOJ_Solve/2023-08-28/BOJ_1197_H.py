import sys,heapq
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)
heap = [[0,1]] # 가중치, 정점번호

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

answer = 0 # 가중치의 합
cnt = 0 # 간선 수

while heap:
    if cnt == v:
        break
    w,s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = 1
        answer += w
        cnt += 1
        for i in graph[s]:
            heapq.heappush(heap,i)
    
print(answer)