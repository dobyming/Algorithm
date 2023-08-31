import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip()) # 배열 사이즈
    arr = list(map(int,input().split()))

    max_val = 0
    tmp = 0
    for i in range(n-1,-1,-1):
        if arr[i] > max_val:
            max_val = arr[i]
        else:
            tmp += max_val - arr[i]
    
    print(tmp)