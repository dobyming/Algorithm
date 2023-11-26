import sys
input = sys.stdin.readline

n = int(input().rstrip())

m_arr = []
for i in range(1,n+1):
    tmp = [n]
    tmp.append(i)

    idx = 1
    while True:
        val = tmp[idx-1] - tmp[idx]
        if val < 0:
            break
        tmp.append(val)
        idx += 1
    
    if len(tmp) > len(m_arr):
        m_arr = tmp
    
print(len(m_arr))
print(*m_arr)