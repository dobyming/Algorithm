n = int(input())
board = [list(input()) for _ in range(n)]
answer = 0

def check(board):
    max_cnt = 1
    # 행 check
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt,cnt)

        cnt = 1
        for j in range(1,n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt,cnt)
    
    return max_cnt

for i in range(n):
    for j in range(n):
        if i+1 < n:
            board[i][j],board[i+1][j] = board[i+1][j],board[i][j]
            cnt = check(board)
            answer = max(answer,cnt)
            board[i][j],board[i+1][j] = board[i+1][j],board[i][j]

        if j+1 < n:
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]
            cnt = check(board)
            answer = max(answer,cnt)
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]

print(answer)