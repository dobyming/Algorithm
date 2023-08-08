import sys,math
input = sys.stdin.readline

n = int(input().rstrip())
arr = [False,False] + [True] * (n-1) 
primes = []

# 에라토스테네스의 체 
for i in range(2,int(math.sqrt(n))+1):
    if arr[i] == True:
        j =2 
        while i*j <= n:
            arr[i*j] = False
            j += 1

for i in range(2,n+1):
    if arr[i] == True:
        primes.append(i)

end = 0
interval_sum = 0
cnt = 0 # 경우의수 

for start in range(len(primes)):
    while end<len(primes) and interval_sum < n:
        interval_sum += primes[end]
        end += 1
    if interval_sum ==  n:
        cnt += 1
    interval_sum -= primes[start]

print(cnt)