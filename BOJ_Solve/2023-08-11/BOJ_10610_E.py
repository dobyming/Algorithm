# N에 있는 숫자들을 적절히 섞어 30배수 중 가장 큰 수 return 

import sys
input = sys.stdin.readline

n = input().rstrip()
n_arr = list(n)
n_arr.sort(reverse=True)

new = int(''.join(n_arr))
if new % 30 == 0:
    print(new)
else:
    print(-1)