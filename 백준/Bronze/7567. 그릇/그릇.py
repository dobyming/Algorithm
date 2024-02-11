import sys
input = sys.stdin.readline

arr = input().rstrip()
answer = 0

for i in range(len(arr)):
    if i == 0:
        answer += 10
    elif arr[i-1] == arr[i]:
        answer += 5
    else:
        answer += 10

print(answer)