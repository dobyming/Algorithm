n = int(input()) # 스위치 개수
# 스위치 초기 상태
status = list(map(int,input().split()))
m = int(input()) # 학생수

for _ in range(m):
    gender,num = map(int,input().split())
    if gender == 1:
        for i in range(num-1,n,num):
            if status[i] == 0:
                status[i] = 1
            else:
                status[i] = 0
    elif gender == 2:
        k = 0
        while num-k-1 >= 0 and num+k-1 < n:
            if status[num-k-1] == status[num+k-1]:
                if status[num-k-1] == 0:
                    status[num-k-1] = 1
                    status[num+k-1] = 1
                else:
                    status[num-k-1] = 0
                    status[num+k-1] = 0
                k += 1
            else:
                break
                
cnt = 0 
for s in status:
    if cnt%20==0 and cnt !=0:
        print()
    print(s,end=" ")
    cnt += 1