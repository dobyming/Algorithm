import sys
input = sys.stdin.readline
# 개총시작,개총종료,스트리밍 종료시간
S,E,Q = input().split()

def calc(time):
    total = 0
    h,m = time.split(':')
    total = int(h)*60+int(m)

    return total

start = calc(S)
end = calc(E)
stream_end = calc(Q)

member = set()
answer = 0
while True:
    try:
        time,name = input().split()
        m_time = calc(time)
        if m_time in range(start+1):
            member.add(name)
        elif m_time in range(end,stream_end+1):
            if name in member:
                answer += 1
                member.remove(name)
    except:
        break

print(answer)