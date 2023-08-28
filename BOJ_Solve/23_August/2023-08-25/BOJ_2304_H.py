import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()
res = 0

# 가장 높은 기둥의 번호
i = 0
for a in arr:
    if a[1] > res:
        res = a[1]
        idx = i
    i+=1

# 초기 높이
l_height = arr[0][1]
# 왼쪽
for i in range(idx):
    if l_height < arr[i+1][1]:
        res += l_height * (arr[i+1][0] - arr[i][0])
        l_height = arr[i+1][1]
    else:
        res += l_height * (arr[i+1][0] - arr[i][0])

# 오른쪽
r_height = arr[-1][1]
for i in range(n-1,idx,-1):
    if r_height < arr[i-1][1]:
        res += r_height * (arr[i][0] - arr[i-1][0])
        r_height = arr[i-1][1]
    else:
        res += r_height * (arr[i][0] - arr[i-1][0])

print(res) 
