import sys
input = sys.stdin.readline

n,m = map(int,input().split())
trees = list(map(int,input().split()))
s,e = 1,max(trees)

while s<=e:
    mid = (s+e) // 2

    tmp = 0
    for tree in trees:
        if tree > mid:
            tmp += (tree-mid)
    
    if tmp >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)