import sys
input= sys.stdin.readline

def solve(start):
    global cnt
    quack = 'quack'
    j = 0
    first = 1 
    for i in range(start,len(sound)):
        if sound[i] == quack[j] and not visited[i]:
            visited[i] = True
            if sound[i] == 'k':
                if first:
                    cnt += 1
                    first = 0
                j = 0 
            # 마지막 문자가 k가 아니면 다음 idx로 넘긴다.
            else:
                j += 1

cnt = 0
sound = input().rstrip()
visited = [False] * (len(sound))

if len(sound) % 5 != 0:
    print(-1)
    exit()

for i in range(len(sound)):
    if sound[i] == 'q' and not visited[i]:
        solve(i)

if cnt == 0 or not all(visited):
    print(-1)
else:
    print(cnt)