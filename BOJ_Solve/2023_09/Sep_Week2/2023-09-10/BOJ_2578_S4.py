board = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]

def check():
    bingo= 0
    # 가로가 빙고일때
    for i in range(5):
        if board[i].count(0) == 5:
            bingo += 1

    # 세로가 빙고일때
    for i in range(5):
        tmp = 0
        for j in range(5):
            if board[j][i] == 0:
                tmp += 1
        if tmp == 5:
            bingo += 1

    right = []  
    left = []  
    for i in range(5):
        right.append(board[i][i])
        left.append(board[i][4 - i])

    if sum(right) == 0:
        bingo += 1
    if sum(left) == 0:
        bingo += 1

    return bingo

count = 0  # 사회자가 숫자를 부른 횟수를 세는 변수
for i in range(5):
    for j in range(5):
        for k in range(5):
            for h in range(5):  
                if nums[i][j] == board[k][h]:  
                    board[k][h] = 0  
                    count += 1  
                if count >= 12:  
                    if check() >= 3:  
                        print(count)  
                        exit()  