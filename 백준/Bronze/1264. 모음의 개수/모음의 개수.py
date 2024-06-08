import sys
input = sys.stdin.readline

vowel = ['a','e','i','o','u','A','E','I','O','U']

while True:
    sentence = input().rstrip()
    cnt = 0
    if sentence == '#':
        break
    for s in sentence:
        if s in vowel:
            cnt += 1
    print(cnt)