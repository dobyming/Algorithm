import sys,math
input = sys.stdin.readline

a,b = map(int,input().split())
if b>10000000:
    b=10000000

p_arr = []
for num in range(a,b+1):
    if str(num) == str(num)[::-1]:
        p_arr.append(num)

def isPrime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

for p in p_arr:
    if isPrime(p):
        print(p)

print(-1)