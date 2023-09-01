import sys
input = sys.stdin.readline

s = input().rstrip()
dp = [[0] * 26]
dp[0][ord(s[0])-97] = 1
# 문자열을 돌때 각 문자에 대해서 알파벳 배열을 하나씩 추가
for i in range(1,len(s)):
    dp.append(dp[-1][:])
    dp[i][ord(s[i])-97] += 1

q = int(input().rstrip())
for _ in range(q):
    alpha,s,e = input().split()
    s,e = map(int,[s,e])

    if s == 0:
        print(dp[e][ord(alpha)-97])
    else:
        print(dp[e][ord(alpha)-97] - dp[s-1][ord(alpha)-97])