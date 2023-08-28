import sys
input = sys.stdin.readline

k,n = map(int,input().split())
arr = [int(input().rstrip()) for _ in range(k)]

s,e = 1,max(arr)
while s<=e:
    mid = (s+e) // 2
    tmp = 0 # 랜선 수

    for i in range(len(arr)):
        tmp += arr[i] // mid
    
    if tmp >= n:
        s = mid + 1
    else:
        e = mid - 1

print(e)