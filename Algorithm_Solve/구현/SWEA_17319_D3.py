# 문자열이 주어질때, 만들어 낼 수 있는지 판단 
T = int(input().rstrip())
for i in range(1,T+1):
    n = int(input().rstrip()) # 문자열의 길이
    s = input().rstrip()

    answer = ''
    if len(s) % 2 != 0 :
        answer = 'No'

    if s[:len(s)//2] == s[len(s)//2:]:
        answer = 'Yes'
    else:
        answer = 'No'
    
    print('#'+str(i)+' '+answer)