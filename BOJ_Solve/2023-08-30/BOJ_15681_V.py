import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur):
    count[cur] = 1
    for i in graph[cur]:
        if not count[i]:
            dfs(i)
            count[cur] += count[i]


# 정점수, 루트번호, 쿼리 수
n,r,q = map(int,input().split())
graph = [[] for _ in range(n+1)]
count = [0] * (n+1)

for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for _ in range(q):
    t = int(input().rstrip())
    print(count[t])
