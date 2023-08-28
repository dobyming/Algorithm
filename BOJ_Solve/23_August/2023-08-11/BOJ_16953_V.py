import sys
input = sys.stdin.readline

a,b = map(int,input().split())

cnt = 1 # 개수 return
while True:
    if b==a:
        print(cnt)
        break
    elif (b%10 != 1 and b%2!=0) or b<a:
        print(-1)
        break
    else:
        if b%10 == 1:
            b = b // 10
        else:
            b = b // 2
        cnt += 1
