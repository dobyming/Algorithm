import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur):
    visited[cur] = 1
    for i in graph[cur]:
        if not visited[i]:
            dfs(i)
            # 현재마을을 우수마을로 선정
            dp[cur][1] += dp[i][0]
            # 현재마을을 우수마을로 선정 안함
            dp[cur][0] += max(dp[i][0],dp[i][1])


n = int(input().rstrip())
arr = [0]+list(map(int,input().split())) # 마을 주민 수 (1번마을: arr[0]명)

visited = [0 for _ in range(n+1)] # 방문 여부 
graph = [[] for _ in range(n+1)] # 마을 인접 정보 

# 각 마을을 우수마을로 선정 여부에 따라 dp 값을 check
# dp[i][0] : 우수마을 선정 안함, dp[i][1]: 우수마을 선정함
dp = [[0,arr[i]]*2 for i in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(max(dp[1][1],dp[1][0]))