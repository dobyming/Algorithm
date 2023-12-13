import sys
input = sys.stdin.readline
from collections import defaultdict

n,d,k,c = map(int,input().split())
arr = [int(input().rstrip()) for _ in range(n)]
answer = -int(1e9)

left,right = 0,k-1
s_dict = defaultdict(int)
# 구간 내에 c는 항상 포함되어 있는다고 가정 
s_dict[c] += 1

for i in range(right+1):
    s_dict[arr[i]] += 1

while left != n:
    answer = max(answer,len(s_dict))
    
    s_dict[arr[left]] -= 1
    if s_dict[arr[left]] == 0:
        del s_dict[arr[left]]
    left += 1

    right += 1
    s_dict[arr[right%n]] += 1

print(answer)