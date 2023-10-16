import sys
input = sys.stdin.readline

# 플레이어 수, 방의 정원(한방에는 m명까지 가능)
p,m = map(int,input().split())
rooms = []

for _ in range(p):
    l,n = input().split()
    if len(rooms) == 0:
        rooms.append([[int(l),n]])
        continue

    flag = False
    for room in rooms:
        # 최초 level 
        if len(room) < m and int(l) in range(-10+room[0][0],room[0][0]+11):
            room.append([int(l),n])
            flag = True
            break
        
    if not flag:
        rooms.append([[int(l),n]])

# 닉네임 순으로 정렬 
for room in rooms:
    room.sort(key=lambda x:x[1])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for a,b in room:
        print(a,b)