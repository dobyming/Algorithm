import sys,math
input = sys.stdin.readline

# 게임횟수, 이긴게임
x,y = map(int,input().split())
win = (y*100) // x
 
if win >= 99:
    print(-1)
else:
    cnt = 0
    left,right = 1,x
    while left <= right:
        mid = (left+right) // 2
        if (y+mid)*100 // (x+mid) <= win:
            left = mid + 1
        else:
            cnt = mid
            right = mid - 1
    print(cnt)