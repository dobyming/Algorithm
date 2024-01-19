import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
graph = [[INF]*26 for _ in range(26)]

# n개의 전제를 깔기
for _ in range(n):
    tmp = input().rstrip().split(" is ")
    a = alphabet.index(tmp[0])
    b = alphabet.index(tmp[1])
    graph[a][b] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

m = int(input().rstrip())
for _ in range(m):
    tmp = input().rstrip().split(" is ")
    a = alphabet.index(tmp[0])
    b = alphabet.index(tmp[1])

    if graph[a][b] == INF:
        print('F')
    else:
        print('T')