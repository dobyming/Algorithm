from collections import defaultdict

T = int(input())
for _ in range(T):
    n = int(input())
    # 의상이름-의상종류(같은 종류의 의상은 하나만 입을 수 있다)
    clothes = [input().split() for _ in range(n)]
    c_dict = defaultdict(list)
    for a,b in clothes:
        c_dict[b].append(a)
    
    answer = 1
    for k in c_dict:
        answer *= (len(c_dict[k])+1)
    
    print(answer-1)