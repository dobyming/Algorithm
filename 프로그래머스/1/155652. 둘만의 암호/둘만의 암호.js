function solution(s, skip, index) {
    var answer = '';
    let alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l'
               ,'m','n','o','p','q','r'
                    ,'s','t','u','v','w','x','y','z'].filter((target) => !skip.includes(target))
    
    let size = alphabet.length;
    for(var i=0; i<s.length; i++) {
        let idx = alphabet.indexOf(s[i])
        answer += alphabet[(idx+index)%size]
    }
    
    return answer;
}