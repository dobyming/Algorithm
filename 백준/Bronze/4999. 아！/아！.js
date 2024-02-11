const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

/**정답 제출 시에는 이 코드로 제출 */
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let jae = input[0].trim();
let doctor = input[1];

jae_len = jae.slice(0,jae.length-1).length;
doc_len = doctor.slice(0,doctor.length-1).length;

jae_len >= doc_len ? console.log('go') : console.log('no');