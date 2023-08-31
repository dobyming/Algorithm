import sys,math
input = sys.stdin.readline 

n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()

cur = 0
answer = 0

for a,b in arr:
    a = max(a,cur)
    cnt = math.ceil((b-a) / l)
    cur = a + cnt * l
    answer += cnt

print(answer)