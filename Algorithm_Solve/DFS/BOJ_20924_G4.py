import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 노드의 개수, 루트노드의 번호
N,R = map(int,input().split())
graph = [{} for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

def r_dfs(node,dist):
    if visited[node]:
        return
    visited[node] = True
    cnt = 0 # 자식 노드 개수
    g1 = 0 # 길이 더하기
    nexts = -1 # 다음 순회돌 노드 번호

    for next in graph[node]:
        if not visited[next]:
            cnt += 1
            nexts = next
            g1 += graph[node][next]

    # 자식이 1개만 있을때
    if cnt == 1:
        return r_dfs(nexts,dist+g1)
    # 자식이 둘 이상이라면 
    else:
        return [node,dist]

def l_dfs(node,dist):
    global giga
    visited[node] = True
    cnt = 0

    for next in graph[node]:
        if not visited[next]:
            cnt += 1
            l_dfs(next,dist+graph[node][next])
    
    if not cnt:
        giga = max(giga,dist)


root_dist = r_dfs(R,0)

giga = 0
l_dfs(root_dist[0],0)

print(root_dist[1],giga)