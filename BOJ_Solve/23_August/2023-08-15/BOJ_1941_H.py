dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(loc):
    global avail
    lx = loc // 5
    ly = loc %5
    for l in range(4):
        nx = lx + dx[l]
        ny = ly + dy[l]
        if not (0<=nx<5 and 0<=ny<5) or visited[nx][ny]:
            continue
        next = nx*5+ny
        if next in tmp:
            visited[nx][ny] = 1
            avail += 1
            check(next)

def dfs(depth,y_cnt,count):
    global cnt,visited,avail

    if y_cnt > 3 or 25-count < 7-depth:
        return
    
    if depth == 7:
        avail = 1
        v_x,v_y = tmp[0]//5, tmp[0]%5
        visited = [[0]*5 for _ in range(5)] # 매조합마다 초기화 필요
        visited[v_x][v_y] = 1 
        check(tmp[0])
        if avail == 7:
            cnt += 1
        return

    i = count // 5
    j = count % 5

    if board[i][j] == 'Y':
        tmp.append(count) 
        dfs(depth+1,y_cnt+1,count+1)
        tmp.pop()
    else:
        tmp.append(count)
        dfs(depth+1,y_cnt,count+1)
        tmp.pop()

    dfs(depth,y_cnt,count+1)


board = [list(input()) for _ in range(5)]
tmp = []
visited = [[0]*5 for _ in range(5)]
cnt = 0
dfs(0,0,0)
print(cnt)