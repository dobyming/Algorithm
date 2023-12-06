import sys
from math import sqrt
input = sys.stdin.readline

n = int(input().rstrip())
# 시간초과 방지
A = set(list(map(int,input().split())))

# 소수 판정
def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

answer = 1
for num in A:
    if isPrime(num):
        answer *= num

if answer == 1:
    answer *= -1

print(answer)