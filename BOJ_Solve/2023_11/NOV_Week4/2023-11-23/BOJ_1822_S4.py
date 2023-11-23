import sys
input = sys.stdin.readline

# 집합 A와 B의 원소 개수
n,m = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

l = len(set(A-B))
answer = list(set(A-B))
answer.sort()

print(l)
if len(answer) != 0:
    print(*answer)