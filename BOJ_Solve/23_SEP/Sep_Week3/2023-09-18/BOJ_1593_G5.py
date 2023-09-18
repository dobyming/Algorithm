import sys
input = sys.stdin.readline

# W의 길이, S의 길이
g,k = map(int,input().split())
w = input().rstrip()
s = input().rstrip()

# 대+소문자 각 alphabet 등장 횟수 
w_arr = [0]*52
s_arr = [0]*52

for i in range(g):
    if 'a'<= w[i] <= 'z':
        w_arr[ord(w[i])-ord('a')] += 1
    else:
        w_arr[ord(w[i])-ord('A')+26] += 1

start,length,cnt = 0,0,0

for j in range(k):
    # 알파벳을 받을때마다 length를 w길이(g) 만큼 잘라준다. 
    if 'a'<= s[j] <= 'z':
        s_arr[ord(s[j])-ord('a')] += 1
    else:
        s_arr[ord(s[j])-ord('A')+26] += 1
    length += 1

    if length == g:
        if w_arr == s_arr:
            cnt += 1
        if 'a' <= s[start] <= 'z':
            s_arr[ord(s[start])-ord('a')] -= 1
        else:
            s_arr[ord(s[start])-ord('A')+26] -= 1
        # g개씩 잘라서 봐야하므로 start 갱신 필요
        start += 1
        length -= 1

print(cnt)