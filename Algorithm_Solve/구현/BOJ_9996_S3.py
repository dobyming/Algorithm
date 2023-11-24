n = int(input())
p = input().split('*')
p_len = len(p[0]) + len(p[1])

for _ in range(n):
    word = input()
    if len(word) < p_len:
        print("NE")
    else:
        if p[0] == word[:len(p[0])] and p[1] == word[-len(p[1]):]:
            print("DA")
        else:
            print("NE")