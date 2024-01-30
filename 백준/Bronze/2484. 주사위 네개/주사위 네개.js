const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input.shift());
let answer = 0;

for (let i=0; i<n; i++) {
  let newArr = input[i].trim().split(' ').map(Number);
  let newMap = new Map();
  let total = 0;

  for (num of newArr) {
    if (!newMap.has(num)) {
      newMap.set(num,1);
    } else {
      newMap.set(num,newMap.get(num)+1);
    }
  }

  newMapArr = [...newMap];
  newMapArr.sort((a,b) => b[1]-a[1]);
  let k_arr = [...newMap.keys()];
  let v_arr = [...newMap.values()];

  for (info of newMapArr) {
    let [k,v] = [info[0],info[1]]
    
    if (v === 4) {
      total = 50000 + k * 5000;
    } 
    else if (v === 3) {
      total = 10000 + k*1000;
      break
    }
    else if (v === 2) {
      let t_cnt = v_arr.filter(elem => elem === 2).length;

      if (t_cnt === 2) {
        total = 2000 + k_arr[0]*500 + k_arr[1]*500;
        break
      } else {
        total = 1000 + k*100;
        break
      }
    } else {
      total = Math.max(...k_arr) * 100
    }
  }
  answer = Math.max(answer,total); 
}
console.log(answer);