import sys
input = sys.stdin.readline

n,k = map(int,input().split())
tmp = k*(k+1)//2

if n < tmp:
    print(-1)
elif (n-tmp) % k == 0:
    print(k-1)
else:
    print(k)