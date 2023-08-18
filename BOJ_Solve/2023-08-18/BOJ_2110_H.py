import sys
input = sys.stdin.readline

n,c = map(int,input().split())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()

answer = 0
s,e = 1,arr[-1]-arr[0]

while s<=e:
    mid = (s+e)//2
    cnt = 1
    cur = arr[0]

    for i in range(1,n):
        if arr[i] >= cur+mid:
            cnt +=1
            cur = arr[i]
    
    if cnt >= c:
        s = mid + 1
        answer = mid
    else:
        e =mid -1

print(answer)             