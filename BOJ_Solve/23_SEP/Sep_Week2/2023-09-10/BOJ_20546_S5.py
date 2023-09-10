def bnp(m,arr):
    total,cnt = 0,0
    for i in range(len(arr)):
        cnt += m // arr[i]
        m = m % arr[i]
    total = m + cnt * arr[-1]
    return total

def timing(m,arr):
    total,cnt = 0,0
    for i in range(len(arr)-4):
        # 3일 연속 증가
        if arr[i] < arr[i+1] < arr[i+2] < arr[i+3]:
            m += cnt * arr[i+3]
            cnt = 0 # 팔았으므로 다시 0으로
        # 3일 연속 감소
        if arr[i] > arr[i+1] > arr[i+2] > arr[i+3]:
            cnt += m // arr[i+3]
            m = m % arr[i+3]
    total = m + cnt * arr[-1]
    return total

money = int(input())
# 주가
rate = list(map(int,input().split()))

bnp_rate, timing_rate = 0,0
bnp_rate = bnp(money,rate)
timing_rate = timing(money,rate)

if bnp_rate > timing_rate:
    print("BNP")
elif bnp_rate < timing_rate:
    print("TIMING")
else:
    print("SAMESAME")