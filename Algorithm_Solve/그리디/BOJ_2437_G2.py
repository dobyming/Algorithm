import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int,input().split()))
arr.sort()

tmp = 1
for k in arr:
    if tmp < k:
        break
    tmp += k

print(tmp)