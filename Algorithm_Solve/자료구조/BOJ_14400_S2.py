import sys
input = sys.stdin.readline

n = int(input().rstrip())
locs = [list(map(int,input().split())) for _ in range(n)]

mid_x = sorted(locs,key=lambda x:x[0])[n//2][0]
mid_y = sorted(locs,key=lambda x:x[1])[n//2][1]

answer = 0
for loc in locs:
    answer += abs(mid_x - loc[0]) + abs(mid_y - loc[1])

print(answer)