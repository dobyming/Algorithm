import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 학생수,친구관계수,가지고 있는 돈 
n,m,k = map(int,input().split())
# 친구비 
cost = [0]+list(map(int,input().split()))

# 부모 테이블
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a != b:
        if cost[a] <= cost[b]:
            parent[b] = a
        else:
            parent[a] = b

# union시 cost가 작은쪽을 root로
for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)

answer = 0
for idx,root in enumerate(parent):
    if idx == root:
        answer += cost[idx] 

if answer <= k:
    print(answer)
else:
    print("Oh no")