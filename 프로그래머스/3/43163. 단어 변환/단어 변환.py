from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    if target not in words:
        answer = 0
        
    q = deque()
    q.append([begin,0]) #단어, 변환 수 
    while q:
        word,cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            tmp_cnt = 0
            if visited[i] == 0:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt += 1
            if tmp_cnt == 1:
                q.append([words[i],cnt+1])
                visited[i] = 1
        
    return answer