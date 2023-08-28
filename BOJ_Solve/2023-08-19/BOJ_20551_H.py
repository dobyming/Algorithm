import sys
input = sys.stdin.readline

def lower_bound(target,arr):
    s,e = 0,len(arr)-1
    while s<=e:
        mid = (s+e) // 2
        if arr[mid] < target:
            s = mid +1
        elif arr[mid] > target:
            e = mid -1
        elif arr[mid] == target:
            if e == mid:
                break
            e = mid
    
    if arr[mid] == target:
        return mid
    else:
        return -1 

n,m = map(int,input().split())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()

for _ in range(m):
    q = int(input().rstrip())
    print(lower_bound(q,arr))