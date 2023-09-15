import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

# 부모테이블 설정
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

# root 노드 찾기
def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    # x의 부모 갱신
    parent[x] = p
    return parent[x]

# a가 속한 집합과 b가 속한 집합을 합치기
def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return 
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    com = list(map(int,input().split()))
    if com[0] == 0:
        union(com[1],com[2])
    elif com[0] == 1:
        if find(com[1]) == find(com[2]):
            print("yes")
        else:
            print("no")