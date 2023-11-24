import sys
input=sys.stdin.readline

n=int(input())
board=[]
for i in range(n):
    board.append(list([input().rstrip() for _ in range(5)]))

answer=[]
for i in range(n-1):
    for j in range(i+1,n):
        cnt=0
        for k in range(5):
            for l in range(7):
                if board[i][k][l]!=board[j][k][l]:
                    cnt+=1
                    
        answer.append((cnt,i+1,j+1))

result=min(answer)
print(result[1],result[2])