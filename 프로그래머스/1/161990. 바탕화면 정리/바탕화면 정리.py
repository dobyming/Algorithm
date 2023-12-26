def solution(wallpaper):
    answer = []
    # x따로 y따로
    loc_x = []
    loc_y = []
    
    for y_idx,row in enumerate(wallpaper):
        for x_idx,target in enumerate(row):
            if target == '#':
                loc_y.append(y_idx)
                loc_x.append(x_idx)
    
    answer = [min(loc_y),min(loc_x),max(loc_y)+1,max(loc_x)+1]
    
    return answer