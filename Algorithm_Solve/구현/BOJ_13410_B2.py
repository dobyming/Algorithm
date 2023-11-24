import sys
input = sys.stdin.readline

# 몇 단, 항의수
n,k = map(int,input().split())

cnt = 1
arr = []
while cnt <= k:
    tmp = n * cnt
    arr.append(tmp)
    cnt += 1

t_arr = list(map(str,arr))
result = []
for t in t_arr:
    rev = t[::-1]
    result.append(int(rev))

print(max(result))