import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def factorial(num):
    return num * factorial(num-1) if num > 1 else 1

n = int(input().rstrip())
result = str(factorial(n))[::-1]

for i in result:
    if i != '0':
        print(i)
        break