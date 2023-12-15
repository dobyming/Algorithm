def solution(s, skip, index):
    answer = ''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l'
               ,'m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for word in skip:
        alphabet.remove(word)
    
    size = len(alphabet)
    for target in s:
        idx = alphabet.index(target)
        answer += alphabet[((idx+index)%size)]
    
    return answer
