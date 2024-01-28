import sys
input = sys.stdin.readline

n,c = map(int,input().split())
arr = list(map(int,input().split()))
result = []

f_dict = {}
for a in arr:
    if a not in f_dict:
        f_dict[a] = 1
    else:
        f_dict[a] += 1

sorted_f = list(f_dict.items())
sorted_f.sort(key=lambda x:x[1] ,reverse=True)

for a,b in sorted_f:
    tmp = 0
    while tmp < b:
        result.append(a)
        tmp += 1
        
print(*result)