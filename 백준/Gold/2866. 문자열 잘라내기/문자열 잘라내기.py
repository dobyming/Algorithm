import sys
input = sys.stdin.readline
from collections import defaultdict

r,c = map(int,input().split())
board = [list(input().rstrip()) for _ in range(r)]

cnt = 0
s,e = 0, r-1
while s<=e:
    # 여기서 mid값은 중복이 걸리기 전의 행을 return 하기 위함
    m = (s+e) // 2

    w_dict = defaultdict(int)
    flag = False
    for j in range(c):
        word = ''
        for i in range(m,r):
            word += board[i][j]
        if word not in w_dict:
            w_dict[word] += 1
        else:
            flag = True
            break
    
    if flag:
        e = m-1
    else:
        cnt = m
        s = m+1
        
        
print(cnt)