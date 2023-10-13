# 자르기 시작했으면, 경로 상의 모든 색종이를 다 잘라야 함
# 이미 자른 곳을 또 자를 순 없음 

# n번 가위질로 k개의 색종이 조각을 만들 수 있는지 여부 return

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
start = 0
end = n // 2
flag = False

while start<=end:
    row = (start+end) // 2
    col = n - row 

    tmp = (row+1) * (col+1)
    if tmp == k:
        print("YES")
        flag = True
        break
    if k > tmp:
        start = row + 1
    else:
        end = row -1

if not flag:
    print("NO")