import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))

# k개의 조를 나누는 법 
tmp = []
for i in range(1,n):
    tmp.append(arr[i]-arr[i-1])

tmp.sort(reverse=True)
print(sum(tmp[k-1:]))