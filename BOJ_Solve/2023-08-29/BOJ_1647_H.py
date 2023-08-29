import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
# 가중치,a,b로 append 후 정렬
graph = []
parent = [i for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append([c,a,b])
graph.sort()

# kruskal 
selected = []
for g in graph:
    cost,a,b = g
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        selected.append(cost)

print(sum(selected[:-1]))