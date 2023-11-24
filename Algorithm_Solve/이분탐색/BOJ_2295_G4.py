import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()

arr_sum = set()
for x in arr:
    for y in arr:
        arr_sum.add(x+y)

answer = 0
for i in range(n-1,-1,-1):
    for j in range(i+1):
        if arr[i] - arr[j] in arr_sum:
            answer = max(answer,arr[i])

print(answer)