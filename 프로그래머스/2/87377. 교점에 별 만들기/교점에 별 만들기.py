from itertools import combinations

def calc(eq1,eq2):
    x1,y1,c1 = eq1
    x2,y2,c2 = eq2
    
    # 평행 또는 일치일때 zd error 방지
    if x1*y2 == y1*x2:
        return 
    
    # 교점 
    X = (y1*c2 - c1*y2) / (x1*y2 - y1*x2)
    Y = (c1*x2 - x1*c2) / (x1*y2 - y1*x2)
    
    if X == int(X) and Y == int(Y):
        return [int(X), int(Y)]

def solution(line):
    answer = []
    meets = []
    # 모든 별을 포함하는 최소한의 크기만 나타내면 된다. 
    # 주어진 다항식을 기준으로 교점을 찾아야함 
    
    # 주어진 line에서 2개의 교점을 찾아야 하는데
    # 그를 위해선 조합이 필요하다.
    for eq1,eq2 in combinations(line,2):
        meet = calc(eq1,eq2)
        if meet:
            meets.append(meet)
    
    r1,r2 = min(meets,key=lambda x:x[0])[0], max(meets,key=lambda x:x[0])[0] + 1
    c1,c2 = min(meets,key=lambda x:x[1])[1], max(meets,key=lambda x:x[1])[1] + 1
    locs = [['.']*(r2-r1) for _ in range(c2-c1)]
    
    for x,y in meets:
        locs[y-c1][x-r1] = '*'
    locs.reverse()
    
    answer = [''.join(loc) for loc in locs]
    
    return answer