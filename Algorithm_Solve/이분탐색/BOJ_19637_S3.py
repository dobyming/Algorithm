import sys
input = sys.stdin.readline

n,m = map(int,input().split())
gijoon = [input().split() for _ in range(n)]

def binary_search(target,arr):
    s,e = 0,len(arr) - 1
    result = 0
    while s<=e:
        mid = (s+e) // 2
        if int(arr[mid][1]) >= target:
            e = mid - 1
            result = mid
        else:
            s = mid + 1
    
    return result 

for _ in range(m):
    val = int(input().rstrip())
    tmp = binary_search(val,gijoon)
    print(gijoon[tmp][0])