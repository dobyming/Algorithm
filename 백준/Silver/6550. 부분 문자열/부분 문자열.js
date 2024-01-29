const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

for (let i=0; i<input.length; i++) {
  const [s,t] = input[i].trim().split(' ');
  
  const sQueue = s.split("");
  
  for (target of t) {
    if (target === sQueue[0]) {
      sQueue.shift();
    }
  }

  console.log(sQueue.length === 0 ? 'Yes' : 'No')
}