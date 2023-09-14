import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int,input().split()))
b,c = map(int,input().split())

cnt = n # 각 시험장 마다 최소 1명의 총감독관은 필요하기 때문 
for i in arr:
    i -= b
    if i > 0:
        if i % c != 0:
            cnt += (i//c) + 1
        else:
            cnt += (i//c)

print(cnt)    