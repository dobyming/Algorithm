import sys 
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(n):
    k -= arr[i]
    if k < 0:
        print(i+1)
        break
else:
    for j in range(n-1,-1,-1):
        k -= arr[j]
        if k < 0:
            print(j+1)
            break