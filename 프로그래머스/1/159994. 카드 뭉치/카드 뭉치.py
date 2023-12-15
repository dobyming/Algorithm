from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    size = len(goal)
    cnt = 0
    # 카드에 적힌 단어들을 활용해 원하는 순서의 단어를 만들 수 있는지 알고싶음 
    for word in goal:
        if word in cards1:
            c1 = cards1.popleft()
            if c1 == word:
                cnt += 1
            else:
                break
        elif word in cards2:
            c2 = cards2.popleft()
            if c2 == word:
                cnt += 1
            else:
                break
    
    if cnt == size:
        answer = "Yes"
    else:
        answer = "No"
        
    return answer