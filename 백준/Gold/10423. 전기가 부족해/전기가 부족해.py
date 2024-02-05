import sys
input = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        parent[b] = a

N,M,K = map(int,input().split())
parent = [i for i in range(N+1)] 
plants = list(map(int,input().split()))

graph = []
for _ in range(M):
    a,b,c = map(int,input().split())
    graph.append([c,a,b])
graph.sort()

for i in range(len(plants)-1):
    union_parent(plants[i],plants[i+1])

result = 0
for g in graph:
    cost,a,b = g
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result += cost

print(result)