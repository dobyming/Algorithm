n,k,p = map(int,input().split())
# 크림 유무
arr = list(map(int,input().split()))
MAX = n*k

answer = 0
for i in range(0,MAX,k):
    if arr[i:i+k].count(0) < p:
        answer += 1
    else:
        continue

print(answer)
