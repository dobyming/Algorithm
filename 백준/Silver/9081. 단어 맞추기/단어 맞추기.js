const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function next_permutation(w){
    let k = -1;
    let m = 0;

    // 가장 큰 k 찾기
    for(let j=0; j<w.length-1; j++){
        if(w[j] < w[j+1]) {
            k = j;
        }
    }
    if(k==-1) {
        return false
    }
    
    // 가장 큰 m 찾기
    for (let l=w.length-1; l >= 0; l--) {
        if(w[k] < w[l]){
            m = l;
            break
        }
    }
    
    // w[k] w[m] swap하기
    let tmp = w[k];
    w[k] = w[m];
    w[m] = tmp;

    // 배열 새로 만들기
    let new_arr = w.slice(0,k+1);
    let rev_arr = w.slice(k+1).reverse()
    let result = new_arr.concat(rev_arr);

    return result
}

let T = Number(input.shift());
for(let i=0; i<T; i++){
    let word = input[i].trim();
    let answer = next_permutation([...word]);

    if(answer) {
        console.log(answer.join(''));
    } else {
        console.log(word);
    }
}