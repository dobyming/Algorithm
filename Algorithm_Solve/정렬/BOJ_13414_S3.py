import sys
input = sys.stdin.readline

# 수강 가능 인원
K,L = map(int,input().split())
l_dict = {}
for i in range(L):
    l_dict[input().rstrip()] = i

l_arr = list(l_dict.items())
l_arr.sort(key=lambda x:x[1])

if K>len(l_arr):
    K = len(l_arr)

for j in range(K):
    print(l_arr[j][0])