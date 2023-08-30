import sys,math
input = sys.stdin.readline
from itertools import permutations

k,m = map(int,input().split())
nums = [i for i in range(10)]
MAX = 10**k
nums_perm = list(permutations(nums,k))

# 소수 배열 전역적으로 만들기
arr = [False,False]+ [True] * (MAX-1)
for i in range(2,int(math.sqrt(MAX))+1):
    if arr[i]:
        j = 2
        while i*j <= MAX:
            arr[i*j] = False
            j += 1

result = 0
for perm in nums_perm:
    if perm[0] == 0:
        continue
    num = int(''.join(list(map(str,perm))))
    tmp = num

    while tmp % m == 0:
        tmp = tmp // m

    for k in range(2,int(math.sqrt(tmp))+1):
        if tmp % k == 0:
            if arr[k] and arr[tmp//k]:
                for l in range(2,num//2):
                    if arr[l] and arr[num-l]:
                        result += 1
                        break
                break
            break

print(result)