function solution(wallpaper) {
    var answer = [];
    let loc_y = []
    let loc_x = []
    
    for(var i=0; i<wallpaper.length; i++){
        for(var j=0; j<wallpaper[i].length; j++){
            if(wallpaper[i][j] === '#'){
                loc_y.push(i)
                loc_x.push(j)
            } 
        }
    }
    // 최솟값
    answer.push(Math.min(...loc_y))
    answer.push(Math.min(...loc_x))
    //최댓값
    answer.push(Math.max(...loc_y)+1)
    answer.push(Math.max(...loc_x)+1)
    
    return answer;
}