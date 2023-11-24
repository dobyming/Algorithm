import sys
input = sys.stdin.readline
from collections import Counter

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]
types = set(arr)

if len(types) == 1:
    print(len(arr))
else:
    answer = []
    length = 0 

    for i in types:
        tmp = 0
        cpy_arr = arr[:]

        # 같은 숫자 제거 
        while i in cpy_arr:
            cpy_arr.remove(i)
        # 가장 긴 부분 계산
        for j in range(1,len(cpy_arr)):
            if cpy_arr[j-1] == cpy_arr[j]:
                tmp += 1
            else:
                length = max(tmp,length)
                tmp = 0
        length = max(tmp,length)
    
    print(length+1)
    