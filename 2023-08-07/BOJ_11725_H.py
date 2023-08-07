import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = start
            dfs(i)

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(1,n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1) # 루트가 1 
for i in range(2,n+1):
    print(visited[i])
