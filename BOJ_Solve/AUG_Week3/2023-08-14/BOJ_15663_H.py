import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs():
    if len(answer) == m:
        print(*answer)
    tmp = 0
    for i in range(n):
        if not visited[i] and tmp != arr[i]:
            visited[i] = 1
            answer.append(arr[i])
            tmp = arr[i]
            dfs()
            visited[i] = 0
            answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
answer = []
visited = [0] * n
dfs()