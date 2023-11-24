import sys,math
sys.setrecursionlimit(10**2)

n = int(input())

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def dfs(prime):
    global answer
    if len(str(prime)) == n:
        print(prime)
    else:
        for i in range(10):
            tmp = prime*10 + i
            if isPrime(tmp):
                dfs(tmp)
        
dfs(2)
dfs(3)
dfs(5)
dfs(7)