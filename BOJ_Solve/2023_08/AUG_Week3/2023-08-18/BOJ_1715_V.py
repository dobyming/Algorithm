import sys,heapq
input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    num = int(input().rstrip())
    heapq.heappush(heap,num)

if len(heap) == 1:
    print(0)
else:
    answer = 0
    while len(heap)>1:
        tmp1 = heapq.heappop(heap)
        tmp2 = heapq.heappop(heap)
        answer += tmp1+tmp2
        heapq.heappush(heap,tmp1+tmp2)
    print(answer)