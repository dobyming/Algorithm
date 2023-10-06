import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(time,idx,value):
    global answer
    value += arr[idx]
    if time == m:
        answer = max(answer,value)
        return
    if idx == n-1:
        answer = max(answer,value)
        return 
    if idx+1 < n:
        dfs(time+1,idx+1,value)
    if idx+2 < n:
        dfs(time+1,idx+2,value//2)

n,m = map(int,input().split())
arr = list(map(int,input().split()))

answer = 0
dfs(1,0,1)
if n>1:
    dfs(1,1,0)
print(answer)