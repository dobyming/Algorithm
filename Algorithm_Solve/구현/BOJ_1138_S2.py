n = int(input().rstrip())
# 각 idx별 내 왼쪽에 몇명이 있었는지에 대한 배열 
arr = list(map(int,input().split()))
# 숫자가 클수록 키가 크다 
tmp = [0] * n

for i in range(n):
    cnt = 0 
    for j in range(n):
        if cnt == arr[i] and tmp[j] == 0:
            tmp[j] = i+1
            break
        elif tmp[j] == 0:
            cnt += 1

print(*tmp)