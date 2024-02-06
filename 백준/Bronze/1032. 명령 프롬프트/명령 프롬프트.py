import sys
input = sys.stdin.readline

# ?에는 아무 문자가 와도 된다. 
# 가능하면 ?를 적게 써야하는 패턴을 return 해야 한다. 

n = int(input().rstrip())
words = [input().rstrip() for _ in range(n)]
f_word = list(words[0])
answer = ''

for i in range(1,n):
    for j in range(len(words[i])):
        if words[i][j] == f_word[j]:
            continue
        else:
            f_word[j] = '?'

print(''.join(f_word))