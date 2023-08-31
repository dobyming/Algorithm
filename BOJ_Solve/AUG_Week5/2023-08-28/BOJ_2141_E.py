import sys
input = sys.stdin.readline

n = int(input().rstrip())
# 위치, 사람수 
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()

total = 0
for a,b in arr:
    total += b

tmp = 0
for i in range(n):
    tmp += arr[i][1]
    if tmp >= total / 2:
        print(arr[i][0])
        break