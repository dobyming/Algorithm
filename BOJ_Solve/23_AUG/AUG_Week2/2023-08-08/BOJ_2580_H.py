def checkRow(x,target):
    for i in range(9):
        if target == board[x][i]:
            return False
    return True

def checkCol(y,target):
    for i in range(9):
        if target == board[i][y]:
            return False
    return True

def checkRect(x,y,target):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if target == board[nx+i][ny+j]:
                return False
    return True

def dfs(cnt):
    if cnt == len(blank):
        for i in range(9):
            print(*board[i])
        exit(0) 
    # 0인 위치의 행,열 위치값 
    for i in range(1,10):
        x = blank[cnt][0]
        y = blank[cnt][1]

        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            board[x][y] = i
            dfs(cnt+1)
            board[x][y] = 0

board = [list(map(int,input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i,j))

dfs(0)