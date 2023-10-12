import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
arr = list(map(int,input().split())) # 소들의 품질 점수
dp = [0] * N
for i in range(N):
    dp[i] = arr[i]*arr[i-1]*arr[i-2]*arr[i-3]

q_arr = list(map(int,input().split())) # 욱제가 바꿀 소 번호

# Q개의 줄에 걸쳐 다시 계산된 S의 값을 출력한다.
answer = sum(dp)

for i in q_arr:
    for j in range(4):
        new_idx = (i-1+j)%N
        dp[new_idx] = -dp[new_idx]
        answer += 2*dp[new_idx]
    print(answer)