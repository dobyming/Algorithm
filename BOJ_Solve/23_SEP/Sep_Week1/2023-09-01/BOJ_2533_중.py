import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(start):
    visited[start] = True
    dp[start][0] = 0
    dp[start][1] = 1 # 얼리어답터 수 

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += min(dp[i][0],dp[i][1])

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# dp[id][1] : 내가 얼리일때, dp[id][0] :얼리가 아닐때
# 각 정점별 2가지로 생각해야한다. 
dp = [[0,0] for _ in range(n+1)]

# 1번 정점
dfs(1)
print(min(dp[1][0],dp[1][1]))