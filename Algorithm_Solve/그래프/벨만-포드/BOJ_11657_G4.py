import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            cur = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]
            if distance[cur] != INF and distance[cur] + cost < distance[next]:
                distance[next] = distance[cur] + cost
                # n번째에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False


n,m = map(int,input().split())
graph = []
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append([a,b,c])

# 벨만-포드
bf_arr = bf(1)

if bf_arr:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])