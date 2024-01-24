import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a_dict = {}

for _ in range(n):
    adrs,pwd = input().split()
    a_dict[adrs] = pwd

for _ in range(m):
    target = input().rstrip()
    print(a_dict[target])