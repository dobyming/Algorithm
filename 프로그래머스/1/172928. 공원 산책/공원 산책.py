def solution(park, routes):
    # answer = []
    N = len(park) # 행
    M = len(park[0]) # 열
    
    sx,sy = 0,0
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                sx,sy = i,j
    
    # 방향            
    dir = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}

    for route in routes:
        route = route.split()
        # 방향,step  
        d,c = route[0],int(route[1])
        
        xx,yy = sx,sy
        isMove = True # 한번에 이동이 가능한지 
        
        for _ in range(c):
            nx = xx+dir[d][0]
            ny = yy+dir[d][1]

            if 0<=nx<N and 0<=ny<M and park[nx][ny] != 'X':
                isMove = True
                xx,yy = nx,ny
            else:
                isMove = False
                break
    
        if isMove:
            sx,sy = nx,ny
            
    return [sx,sy]