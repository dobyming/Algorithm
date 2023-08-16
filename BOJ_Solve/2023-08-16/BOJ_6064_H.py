# m과n보다 작은 두 개의 자연수 x,y로 각 년도를 표시
# x<M : x+1로 표시 , y<N: y+1로 표시
# x,y값이 M을 초과하는순간 다시 1로 초기화해서 count  
# 첫번째 해 : 1:1 두번쨰 해: 2:2 
# <10:12> : 60번째해(마지막 해)

import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    m,n,x,y = map(int,input().split())
    k = x 
    while k <= m*n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            print(k)
            break
        k += m 
    else:
        print(-1)