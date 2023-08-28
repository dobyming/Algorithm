n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y,n):
    global r1,r2,r3
    tmp = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j] != tmp:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3,y+l*n//3,n//3)
                return
    
    if tmp == -1:
        r1 += 1
    elif tmp == 0:
        r2 += 1
    else:
        r3 += 1

# -1,0,1 개수
r1,r2,r3=0,0,0
dfs(0,0,n)

print(r1)
print(r2)
print(r3)