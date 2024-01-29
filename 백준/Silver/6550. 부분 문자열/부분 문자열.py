import sys
input = sys.stdin.readline

while True:
    try:
        s,t = input().split()
        
        s_idx = 0
        cnt = 0 
        flag = False
        for i in range(len(t)):
            if t[i] == s[s_idx]:
                s_idx += 1
                cnt += 1
            if cnt == len(s):
                flag = True
                break
        
        if flag:
            print("Yes")
        else:
            print("No")
    
    except:
        break