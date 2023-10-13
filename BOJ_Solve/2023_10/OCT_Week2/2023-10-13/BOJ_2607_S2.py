n = int(input())
target = list(input())
arr = [input() for _ in range(n-1)]
cnt = 0

for a in arr:
    cp = target[:]
    tmp = 0 
    for w in a:
        if w in cp:
            cp.remove(w)
        else:
            tmp += 1
    if tmp < 2 and len(cp) < 2:
        cnt += 1
    
print(cnt)