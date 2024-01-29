import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [input().rstrip()[::-1] for _ in range(n)]

k = 0
while True:
    s_dict = {}
    for a in arr:
        if a[:k+1] not in s_dict:
            s_dict[a[:k+1]] = 1
        # 만약 동일한 값이 하나라도 있다면 엎어침(k만 늘림)
        else:
            s_dict = {}
            k = k+1
    # 다 1개씩만 존재하고 n명일때
    if list(s_dict.values()).count(1) == n:
        break

print(k+1)