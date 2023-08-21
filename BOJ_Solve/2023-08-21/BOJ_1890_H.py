import sys
input = sys.stdin.readline

n = int(input().rstrip())
board = [list(map(int,input().split())) for _ in range(n)]

# dp 2차원 배열 선언하기 
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            exit(0)
        cur = board[i][j]
        # 오른쪽으로 이동하기
        if j + cur < n:
            dp[i][j+cur] += dp[i][j]
        # 아래쪽으로 이동하기
        if i + cur < n:
            dp[i+cur][j] += dp[i][j]