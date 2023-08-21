import sys
input = sys.stdin.readline

def dfs(cnt):
    global answer
    if cnt == len(num):
        print(*answer)
        exit()
    
    tmp1 = int(num[cnt])
    if not visited[tmp1]:
        visited[tmp1] = 1
        answer.append(tmp1)
        dfs(cnt+1)
        visited[tmp1] = 0
        answer.pop()
    
    if cnt+1 < len(num):
        tmp2 = int(num[cnt:cnt+2])
        if tmp2 <= n and not visited[tmp2]:
            visited[tmp2] = 1
            answer.append(tmp2)
            dfs(cnt+2)
            visited[tmp2] = 0
            answer.pop()

# 최대 수용할 수 있는 n값을 구하는 방법
num = input().rstrip()

n = 0
if len(num) > 10:
    n = 9+(len(num)-9)//2
else:
    n = len(num)

answer = []
visited = [0] * (n+1)
dfs(0)