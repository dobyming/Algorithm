import sys
input = sys.stdin.readline

n = int(input().rstrip())
men = list(map(int,input().split()))
women = list(map(int,input().split()))

men.sort()
women.sort()

s,e = 0,n-1
cnt = 0

while s<n and 0<=e:
    if men[s] < 0 and women[e] >0:
        if abs(men[s]) > women[e]:
            cnt += 1
            s += 1
            e -= 1
        elif abs(men[s]) <= women[e]:
            e -= 1
    elif men[s] > 0 and women[e] < 0:
        if abs(women[e]) > men[s]:
            cnt += 1
            s += 1
            e -= 1
        elif abs(women[e]) <= men[s]:
            e -= 1
    elif men[s]<0 and women[e]<0:
        s += 1
    elif men[s] >0 and women[e]>0:
        e -= 1

print(cnt)