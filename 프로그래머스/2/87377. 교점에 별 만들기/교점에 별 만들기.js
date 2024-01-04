function calc(eq1,eq2){
    let A = eq1[0]
    let B = eq1[1]
    let E = eq1[2]
    
    let C = eq2[0]
    let D = eq2[1]
    let F = eq2[2]
    
    if(A*D === B*C){
        return
    }
    let X = (B*F - E*D) / (A*D - B*C)
    let Y = (E*C - A*F) / (A*D - B*C)
    
    if(Number.isInteger(X) && Number.isInteger(Y)){
        return [parseInt(X),parseInt(Y)]
    }
}

function solution(line){
    let meets = [];
    // 교점 구하기 
    for(let i=0; i<line.length; i++){
        for(let j=i+1; j<line.length; j++){
            let eq1 = [line[i][0],line[i][1],line[i][2]]
            let eq2 = [line[j][0],line[j][1],line[j][2]]
            // meet의 return은 배열의 형태일것 
            let meet = calc(eq1,eq2)
            if(meet){
                meets.push(meet)
            }
        }
    }
    
    let x_meets = []
    let y_meets = []
    for(meet of meets){
        x_meets.push(meet[0])
        y_meets.push(meet[1])
    }
    
    // 보드판 setting
    let r1 = Math.min(...x_meets)
    let r2 = Math.max(...x_meets) + 1
    let c1 = Math.min(...y_meets)
    let c2 = Math.max(...y_meets) + 1
    
    let locs = Array.from(Array(c2-c1),() => Array(r2-r1).fill('.')) 
    
    for(meet of meets){
        let x = meet[0]
        let y = meet[1]
        locs[y-c1][x-r1] = '*'
    }
    locs.reverse()

    return locs.map((loc) => loc.join(""))
}