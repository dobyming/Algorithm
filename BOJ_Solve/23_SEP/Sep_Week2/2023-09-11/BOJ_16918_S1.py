from collections import deque
# N초가 지난 후의 격자판 결과를 return 
R,C,N = map(int,input().split())
board = [list(input()) for _ in range(R)]
queue = deque([])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 폭탄 터트리기
def bfs(q,board):
    while q:
        x,y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C and board[nx][ny] == 'O':
                board[nx][ny] = '.'    

def bomb(t):
    global queue,board
    if t == 1:
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    queue.append([i,j])
    # 폭탄은 홀수초에 터진다
    elif t%2 == 1:
        bfs(queue,board)
        # 계속해서 폭탄터질 위치 잡기 
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    queue.append([i,j])
    # 짝수초에는 모든 칸을 폭탄으로 바꾼다
    else:
        board = [['O']*C for _ in range(R)]

for i in range(1,N+1):
    bomb(i)

for b in board:
    print(''.join(b))