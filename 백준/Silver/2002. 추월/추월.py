import sys
input = sys.stdin.readline
from collections import deque

# 터널 내부에선 추월이 불가능 
# 대근: 터널입구, 영식: 터널출구에 위치 
# 대근: 차가 들어가는 순서 기록, 영식: 차가 나오는 순서 기록
# 각각의 기록을 보고 난 후, 추월했을 차의 개수를 return 

s_rec = {}
out = []
answer = 0

n = int(input().rstrip())
for i in range(n):
    in_car = input().rstrip()
    s_rec[in_car] = i

out = [input().rstrip() for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if s_rec[out[i]] > s_rec[out[j]]:
            answer += 1
            break

print(answer)