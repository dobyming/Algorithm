import sys
input = sys.stdin.readline

R,C = map(int,input().split())
board = [list(input().rstrip()) for _ in range(R)]
tmp = []

# 행일때
for i in range(R):
    word = ''
    for j in range(C):
        if board[i][j] != '#':
            word += board[i][j]
        else:
            if len(word) >= 2:
                tmp.append(word)
                word = ''
            else:
                word = ''
                continue
    if len(word) > 1:
        tmp.append(word)

# 열일때
z_board = list(map(list,zip(*board)))
for i in range(C):
    word = ''
    for j in range(R):
        if z_board[i][j] != '#':
            word += z_board[i][j]
        else:
            if len(word) >= 2:
                tmp.append(word)
                word = ''
            else:
                word = ''
                continue
    if len(word) > 1:
        tmp.append(word)

tmp.sort()
print(tmp[0])