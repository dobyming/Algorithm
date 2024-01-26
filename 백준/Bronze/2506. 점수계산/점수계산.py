import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int,input().split()))

cnt = 0
result = 0
for i in range(n):
    if arr[i] == 1:
        cnt += 1
        result += cnt
    else:
        cnt = 0

print(result)