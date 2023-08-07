import sys
input = sys.stdin.readline

def find_min(curr, cost, cnt):
    global answer
    if N == cnt:
        answer = min(answer, cost)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            find_min(i, cost + board[curr][i], cnt+1)
            visited[i] = 0

N,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [0] * N
visited[K] = 1
answer = int(1e9)

for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

find_min(K, 0, 1)
print(answer)