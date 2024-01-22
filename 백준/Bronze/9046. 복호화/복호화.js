const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

/**정답 제출 시에는 이 코드로 제출 */
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let n = input.shift();
for(let i=0; i<n; i++){
    let target = input[i].trim().split(" ")
    let t_map = new Map();
    let a = []

    target.forEach((word) => {
        for(let j=0; j<word.length; j++){
            t_map.set(word[j],(t_map.get(word[j])||0)+1);
        }
    })
    
    let max_val = Math.max(...t_map.values());
    t_map.forEach((value,key) => {
        if(value === max_val) {
            a.push(key);
        }
    });
    
    if(([...t_map.values()].length) === 0 || a.length>1){
        console.log('?');
    } else {
        console.log(a[0]);
    }
}