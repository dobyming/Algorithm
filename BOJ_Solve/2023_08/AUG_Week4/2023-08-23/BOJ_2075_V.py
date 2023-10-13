import sys,heapq
input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    numbers = list(map(int,input().split()))

    if len(heap) == 0:
        for num in numbers:
            heapq.heappush(heap,num)
    
    else:
        for num in numbers:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap,num)

print(heap[0])