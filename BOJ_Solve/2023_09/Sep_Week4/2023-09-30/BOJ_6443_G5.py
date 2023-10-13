import sys
input = sys.stdin.readline
sys.setrecursionlimit(100)

def dfs(cnt):
    if cnt == len(word):
        print(''.join(answer))
        return
    
    for j in visited:
        if visited[j]:
            visited[j] -= 1
            answer.append(j)
            dfs(cnt+1)
            visited[j] += 1
            answer.pop()

n = int(input().rstrip())
for _ in range(n):
    word = list(input().rstrip())
    word.sort()
    visited = {} # 각 단어별 개수 
    answer = [] # 각 단어 조합

    # 백트래킹에 참고 
    for i in word:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1
    
    dfs(0)