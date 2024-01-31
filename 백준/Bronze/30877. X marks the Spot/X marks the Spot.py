import sys
input = sys.stdin.readline

n = int(input().rstrip())
answer = ''

def change(target):
    if 97<=ord(target)<=122:
        return chr(ord(target)-32)
    else:
        return target

for _ in range(n):
    s,t = input().split()

    for i in range(len(s)):
        if s[i] == 'x' or s[i] == 'X':
            print(str(change(t[i])),end='')
            break
            
print(answer)