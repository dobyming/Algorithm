import sys,heapq
input = sys.stdin.readline

n = int(input().rstrip())
l = [list(map(int,input().split())) for _ in range(n)]
l.sort()

heap = []
heapq.heappush(heap,l[0][1])

for i in range(1,n):
    if heap[0] <= l[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap,l[i][1])
    else:
        heapq.heappush(heap,l[i][1])

print(len(heap))