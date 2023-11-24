from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    # 그래프 만들기
    graph = [[] for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [-1] * (n+1)
    queue = deque([destination])
    visited[destination] = 0
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                queue.append(i)
    
    for source in sources:
        answer.append(visited[source])
        
    return answer