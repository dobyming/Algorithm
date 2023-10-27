n = int(input())
# 왼쪽용
arr = [int(input()) for _ in range(n)]
# 오른쪽용
r_arr = arr[::-1]

l_cnt,r_cnt = 0,0
l_max,r_max = 0,0

for l in arr:
    if l_max < l:
        l_max = l
        l_cnt += 1

for r in r_arr:
    if r_max < r:
        r_max = r
        r_cnt += 1

print(l_cnt)
print(r_cnt)