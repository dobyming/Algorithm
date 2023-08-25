import sys
input = sys.stdin.readline

# 식탁의 길이, 선택 거리
n,k = map(int,input().split())
arr = list(input().rstrip())

answer = 0
for i in range(n):
    if arr[i] == 'P':
        for j in range(max(i-k,0),min(k+i+1,n)):
            if arr[j] == 'H':
                arr[j] = ''
                answer += 1
                break

print(answer)