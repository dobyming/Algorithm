import sys
input = sys.stdin.readline

n = int(input().rstrip())
scores = [int(input().rstrip()) for _ in range(n)]

cnt = 0
for i in range(n-2,-1,-1):
    if scores[i] >= scores[i+1]:
        cnt += scores[i] - scores[i+1] + 1
        scores[i] = scores[i+1] - 1
    else:
        continue

print(cnt)