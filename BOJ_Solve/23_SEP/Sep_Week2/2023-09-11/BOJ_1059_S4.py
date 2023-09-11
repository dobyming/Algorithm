l = int(input())
S = list(map(int,input().split()))
n = int(input())

S.append(0)
S.sort()

cnt = 0 # 좋은 구간 개수 
for i in range(len(S)-1):
    if S[i] == n or S[i+1] == n:
        cnt = 0
        break
    elif S[i] < n and n < S[i+1]:
        cnt = (n-S[i]) * (S[i+1]-n) - 1
        break

print(cnt)