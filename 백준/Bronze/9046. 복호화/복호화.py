import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    answer = []
    t_dict = {}

    target = input().rstrip()
    t_arr = target.split(' ')

    for t in t_arr:
        for i in t:
            if i not in t_dict:
                t_dict[i] = 1
            else:
                t_dict[i] += 1
    
    answer = sorted(t_dict.values() ,reverse=True)
    if (len(answer)>1 and answer[0]==answer[1]) or len(answer) == 0:
        print('?')
    else:
        print(max(t_dict,key=t_dict.get))