n = int(input().rstrip())
answer = []

for _ in range(n):
    word = input().rstrip()
    tmp = ''

    for w in word:
        if w.isdigit():
            tmp += w
        else:
            # 숫자-문자 조합이 나올때
            if tmp:
                answer.append(int(tmp))
                tmp = ''
    # 숫자만 있을때
    if tmp:
        answer.append(int(tmp))

answer.sort()
for ans in answer:
    print(ans)