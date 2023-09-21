import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(start,depth):
    global flag
    visited[start] = 1
    if depth == 5:
        flag = True
        return
    for i in graph[start]:
        if not visited[i]:
            dfs(i,depth+1)
    visited[start] = 0
            
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [0] * n
flag = False

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i,1)
    if flag:
        break

if flag:
    print(1)
else:
    print(0)