from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)] # 1번 노드로 계산 
    distance = [-1] * (n+1)
    queue = deque([])
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # bfs 
    def bfs(start):
        queue.append(start)
        distance[start] = 0

        while queue:
            now = queue.popleft()
            for i in graph[now]:
                if distance[i] == -1:
                    queue.append(i)
                    distance[i] = distance[now] + 1

    bfs(1)
    max_length = max(distance)
    for d in distance:
        if d == max_length:
            answer += 1
    
    return answer