def solution(users, emoticons):
    answer = [0,0]
    # 이모티콘에 할인 비율을 어떻게 산정할 것인가? => 모든 할인 비율의 경우의 수를 적용?
    rate = [10,20,30,40]
    discount = []

    # 모든 경우의 할인율을 적용하기
    def dfs(temp,depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        else:
            for i in rate:
                temp[depth] += i
                dfs(temp,depth+1)
                temp[depth] -= i
    
    # emoticon 배열의 크기만큼 경우의 수 완탐하기 
    dfs([0]*len(emoticons),0)

    for disc in discount:
        # 가입자 수, 판매액 
        cnt, result = 0,0
        for user in users:
            pay = 0
            for j in range(len(disc)):
                if disc[j] >= user[0]:
                    pay += emoticons[j] * (100-disc[j])/100
                # 임티 플러스에 가입 하는게 맞음
                if pay >= user[1]:
                    break
            if pay >= user[1]:
                pay = 0
                cnt += 1
            result += pay
        
        if cnt >= answer[0]:
            if cnt == answer[0]:
                answer[1] = max(answer[1],result)
            else:
                answer[1] = result
            answer[0] = cnt 
            
    return answer