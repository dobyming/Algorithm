def check(last,cur):
    last_row = int(last[1]) - 1
    last_col = ord(last[0]) - 65
    cur_row = int(cur[1]) -1
    cur_col = ord(cur[0]) - 65

    if abs(last_col-cur_col) ==2 and abs(last_row-cur_row) == 1:
        return True
    elif abs(last_col-cur_col) ==1 and abs(last_row-cur_row) == 2:
        return True
    else:
        return False
    
se = []
now = input()
se.append(now)

cnt = 1
for _ in range(35):
    dst = input()
    se.append(dst)

    # 이전, 지금
    if check(now,dst):
        cnt += 1
        now = dst 
    else:
        break

if cnt == 36 and len(set(se)) == 36 and check(se[0],se[-1]):
    print("Valid")
else:
    print("Invalid")