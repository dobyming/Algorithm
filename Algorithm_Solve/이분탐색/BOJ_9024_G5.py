import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    
    min_val = 200000000
    for i in range(n):
        s = i+1
        e = n-1
        while s<=e:
            mid = s + (e-s) // 2
            tmp = arr[i] + arr[mid]
            if tmp > k:
                e = mid - 1
            else:
                s = mid + 1
            if abs(tmp-k) < min_val:
                min_val = abs(tmp-k)
                cnt = 1
            elif abs(tmp-k) == min_val:
                cnt += 1
    
    print(cnt)