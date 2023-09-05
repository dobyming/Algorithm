import sys
input = sys.stdin.readline

# 끊어진 개수, 기타줄 브랜드 개수
n,m = map(int,input().split())
brand = [list(map(int,input().split())) for _ in range(m)]

six = sorted(brand,key=lambda x:x[0])
one = sorted(brand,key=lambda x:x[1])

answer = 0
if six[0][0] <= one[0][1] * 6:
    answer = six[0][0] * (n//6) + one[0][1] * (n%6)
    if six[0][0] < one[0][1] * (n%6):
        answer = six[0][0] * (n//6+1)
else:
    answer = one[0][1] * n

print(answer)