import sys
input = sys.stdin.readline

n,m = map(int,input().split())
cards = list(map(int,input().split()))

cnt = 0 # m번 연산 카운트 

while cnt != m:
    cards.sort()
    tmp = cards[0] + cards[1]
    
    cards[0],cards[1] = tmp, tmp
    cnt += 1

print(sum(cards))