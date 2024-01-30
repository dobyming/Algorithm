import sys
input = sys.stdin.readline

n = int(input().rstrip())
answer = 0
for _ in range(n):
    dice = {}
    row = list(map(int,input().split()))
    for r in row:
        if r not in dice:
            dice[r] = 1
        else:
            dice[r] += 1
    
    dice_arr = list(dice.items())
    dice_arr.sort(key=lambda x:x[1], reverse=True)
    
    for key,value in dice_arr:
        if value == 4:
            total = 50000 + key*5000
        elif value == 3:
            total = 10000 + key*1000
            break
        elif value == 2:
            if list(dice.values()).count(2) == 2:
                tmp = list(dice.keys())
                total = 2000 + tmp[0] * 500 + tmp[1] * 500
                break
            else:
                total = 1000 + key * 100
        elif list(dice.values()).count(1) == 4:
            tmp = max(list(dice.keys()))
            total = tmp * 100

    answer = max(answer,total)

print(answer)