import sys
input = sys.stdin.readline

n = int(input().rstrip())
tips = [int(input().rstrip()) for _ in range(n)]
# 큰거먼저
tips.sort(reverse=True)

answer = 0
for i in range(n):
    tmp = tips[i] - i
    if tmp < 0:
        tmp = 0
    answer += tmp

print(answer)