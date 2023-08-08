from itertools import combinations

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
answer = int(1e9)

# 집 주소 따기 
house_loc = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house_loc.append([i,j])


# m개의 치킨집을 최대 골랐을때 도시의 치킨 거리의 최솟값 
chick_loc = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chick_loc.append([i,j])

chick_loc_comb = list(combinations(chick_loc,m))
for comb in chick_loc_comb:
    tmp = 0
    for house in house_loc:
        chicken_len = 999
        # 하나의 집에서 가장 가까운 치킨집 거리 구하기
        for j in range(m):
            chicken_len = min(chicken_len,abs(house[0]-comb[j][0])+abs(house[1]-comb[j][1]))
        tmp += chicken_len
    answer = min(answer,tmp)

print(answer)