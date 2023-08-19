import sys
input = sys.stdin.readline

def binary_search(arr,start,end):
    while start<=end:
        mid = (start+end) // 2
        tmp = 0
        for i in range(len(arr)):
            if mid >= arr[i]:
                tmp += arr[i]
            else:
                tmp += mid

        if tmp <= m:
            start = mid + 1
        else:
            end = mid - 1
    
    return end 

n = int(input().rstrip())
arr = list(map(int,input().split()))
m = int(input().rstrip()) # 국가 예산 

if sum(arr) <= m:
    print(max(arr))
else:
    s,e = 1,max(arr)
    print(binary_search(arr,s,e))