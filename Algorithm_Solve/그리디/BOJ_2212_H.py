import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
road = list(map(int,input().split()))

if k>=n:
    print(0)
    sys.exit()

road.sort()
sub = []
for i in range(n-1):
    sub.append(abs(road[i+1]-road[i]))

sub.sort(reverse=True)
for _ in range(k-1):
    sub.pop(0)
    
print(sum(sub))