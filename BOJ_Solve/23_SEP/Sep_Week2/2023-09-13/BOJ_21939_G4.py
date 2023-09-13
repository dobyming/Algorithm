import sys,heapq
input = sys.stdin.readline

n = int(input().rstrip())
# 문제번호,난이도 순서
min_heap = []
max_heap = []
in_dict = {}

for _ in range(n):
    p,l = map(int,input().split())
    heapq.heappush(min_heap,[l,p])
    heapq.heappush(max_heap,[-l,-p])
    in_dict[p] = True

m = int(input().rstrip())
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'recommend':
        if cmd[1] == '1':
            while not in_dict[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while not in_dict[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])

    elif cmd[0] == 'solved':
        in_dict[int(cmd[1])] = False

    else:
        num = int(cmd[1])
        sq = int(cmd[2])
        
        while not in_dict[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        while not in_dict[min_heap[0][1]]:
            heapq.heappop(min_heap)
        in_dict[num] = True
        heapq.heappush(max_heap,[-sq,-num])
        heapq.heappush(min_heap,[sq,num])